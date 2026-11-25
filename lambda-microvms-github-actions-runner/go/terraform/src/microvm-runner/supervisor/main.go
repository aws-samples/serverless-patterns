package main

import (
	"context"
	"errors"
	"log"
	"net/http"
)

func main() {
	ctx := context.Background()

	s, err := NewSupervisor(ctx)
	if err != nil {
		log.Fatalf("failed to create supervisor: %v", err)
	}

	log.Printf("supervisor starting on %s", s.port)

	// The shutdown after self-termination returns http.ErrServerClosed.
	if err := s.Run(ctx); err != nil && !errors.Is(err, http.ErrServerClosed) {
		log.Fatalf("supervisor exited with error: %v", err)
	}

	log.Printf("supervisor stopped")
}
