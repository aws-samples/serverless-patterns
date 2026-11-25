package main

import (
	"context"
	"encoding/json"
	"log"
	"net/http"
	"sync"
	"time"

	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/lambdamicrovms"
)

type Supervisor struct {
	mvmClient *lambdamicrovms.Client
	port      string

	microvmID      string
	runHookPayload string // presigned S3 GET URL for the JIT config

	done chan struct{}
	once sync.Once
}

func NewSupervisor(ctx context.Context) (*Supervisor, error) {
	cfg, err := config.LoadDefaultConfig(ctx)
	if err != nil {
		return nil, err
	}

	s := &Supervisor{
		mvmClient: lambdamicrovms.NewFromConfig(cfg),
		port:      ":8080",
		done:      make(chan struct{}),
	}
	return s, nil
}

func (s *Supervisor) Run(ctx context.Context) error {
	ctx, cancel := context.WithCancel(ctx)
	defer cancel()

	mux := http.NewServeMux()
	mux.HandleFunc("/aws/lambda-microvms/runtime/v1/run", s.handleRun)
	mux.HandleFunc("/aws/lambda-microvms/runtime/v1/ready", s.handleReady)
	// Both handlers reply immediately (the job runs in a goroutine), so these
	// fit inside the 30s hook timeouts in main.tf.
	server := &http.Server{
		Addr:              s.port,
		Handler:           mux,
		ReadHeaderTimeout: 5 * time.Second,
		ReadTimeout:       10 * time.Second,
		WriteTimeout:      10 * time.Second,
		IdleTimeout:       60 * time.Second,
	}

	go func() {
		<-s.done
		server.Shutdown(ctx)
	}()

	return server.ListenAndServe()

}

func (s *Supervisor) handleRun(w http.ResponseWriter, r *http.Request) {

	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}

	var req RunHookRequest
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		http.Error(w, "failed to decode request body", http.StatusBadRequest)
		return
	}

	if req.MicrovmID == "" {
		http.Error(w, "missing microvmId", http.StatusBadRequest)
		return
	}

	s.once.Do(func() {
		s.microvmID = req.MicrovmID
		s.runHookPayload = req.RunHookPayload
		go s.runJobAndTerminate(context.Background())
	})
	w.WriteHeader(http.StatusOK)

}

// handleReady answers the build-time /ready hook. The supervisor is ready once
// its server accepts connections, so Lambda can snapshot right away.
func (s *Supervisor) handleReady(w http.ResponseWriter, r *http.Request) {
	w.WriteHeader(http.StatusOK)
}

// runJobAndTerminate runs one job, then self-terminates on every exit path.
// The /run hook fires on an already-resumed snapshot, so boot time is not
// included in these timings.
func (s *Supervisor) runJobAndTerminate(ctx context.Context) {
	t0 := time.Now()
	log.Printf("timing: job start microvmID=%s", s.microvmID)

	tResolve := time.Now()
	jitConfig, err := s.resolveJitConfig(ctx, s.runHookPayload)
	log.Printf("timing: jit resolve took %s", time.Since(tResolve).Round(time.Millisecond))

	if err != nil {
		log.Printf("could not resolve JIT config: %v (terminating anyway)", err)
	} else {
		tRun := time.Now()
		rerr := runGitHubRunner(ctx, jitConfig)
		log.Printf("timing: runner (job) took %s", time.Since(tRun).Round(time.Millisecond))
		if rerr != nil {
			log.Printf("runner failed: %v (terminating anyway)", rerr)
		} else {
			log.Printf("job done, terminating self")
		}
	}

	tTerm := time.Now()
	if err := s.terminateSelf(ctx); err != nil {
		log.Printf("terminate failed: %v", err)
	}
	log.Printf("timing: terminate call took %s", time.Since(tTerm).Round(time.Millisecond))
	log.Printf("timing: total /run -> terminate %s", time.Since(t0).Round(time.Millisecond))

	close(s.done)

}

func (s *Supervisor) terminateSelf(ctx context.Context) error {
	ctx, cancel := context.WithTimeout(ctx, 15*time.Second)
	defer cancel()

	_, err := s.mvmClient.TerminateMicrovm(ctx, &lambdamicrovms.TerminateMicrovmInput{
		MicrovmIdentifier: &s.microvmID,
	})
	return err
}
