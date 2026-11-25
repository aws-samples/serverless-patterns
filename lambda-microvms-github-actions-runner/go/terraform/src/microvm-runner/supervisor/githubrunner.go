package main

import (
	"context"
	"errors"
	"fmt"
	"io"
	"net/http"
	"os"
	"os/exec"
	"path/filepath"
	"time"
)

const runnerDirEnv = "RUNNER_DIR"

// The timeout bounds a stalled S3 GET so the VM still self-terminates
// (http.DefaultClient has no timeout).
var jitHTTPClient = &http.Client{Timeout: 30 * time.Second}

// resolveJitConfig fetches the JIT config from the presigned S3 URL in the /run
// hook payload, so the MicroVM needs no S3 permissions.
func (s *Supervisor) resolveJitConfig(ctx context.Context, url string) (string, error) {
	if url == "" {
		return "", errors.New("empty pre-signed URL in run hook payload")
	}

	req, err := http.NewRequestWithContext(ctx, http.MethodGet, url, nil)
	if err != nil {
		return "", fmt.Errorf("build JIT request: %w", err)
	}

	resp, err := jitHTTPClient.Do(req)
	if err != nil {
		return "", fmt.Errorf("fetch JIT config: %w", err)
	}
	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return "", fmt.Errorf("read JIT config body: %w", err)
	}
	if resp.StatusCode != http.StatusOK {
		// Never log the URL or body: the URL is a bearer credential.
		return "", fmt.Errorf("JIT fetch returned HTTP %d", resp.StatusCode)
	}

	return string(body), nil
}

// runGitHubRunner runs the single-use JIT runner and blocks until its one job
// completes.
func runGitHubRunner(ctx context.Context, jitConfig string) error {
	if jitConfig == "" {
		return errors.New("empty JIT config: nothing to run")
	}

	runnerDir := os.Getenv(runnerDirEnv)
	if runnerDir == "" {
		return fmt.Errorf("%s not set; cannot locate the Actions runner", runnerDirEnv)
	}

	runScript := filepath.Join(runnerDir, "run.sh")
	if _, err := os.Stat(runScript); err != nil {
		return fmt.Errorf("runner entrypoint %s not found: %w", runScript, err)
	}

	cmd := exec.CommandContext(ctx, runScript, "--jitconfig", jitConfig)
	cmd.Dir = runnerDir

	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr

	cmd.Env = os.Environ()

	if err := cmd.Run(); err != nil {
		return fmt.Errorf("runner exited with error: %w", err)
	}
	return nil
}
