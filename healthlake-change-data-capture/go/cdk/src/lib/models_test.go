package lib

import (
	"testing"
	"time"

	"github.com/segmentio/ksuid"
)

func Test_ShouldBuildIdempotencyKey(t *testing.T) {
	// arrange
	id := ksuid.New().String()
	resourceType := "Patient"
	now := time.Date(2022, 1, 4, 0, 0, 0, 0, time.UTC)

	// act
	key := BuildIdempotencyKey(resourceType, id, now)

	//
	t.Logf("(Key)=%s", key)
}
