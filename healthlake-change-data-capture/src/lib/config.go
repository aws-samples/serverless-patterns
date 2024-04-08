package lib

import (
	ddlambda "github.com/DataDog/datadog-lambda-go"
)

func DataDogConfig() *ddlambda.Config {
	return &ddlambda.Config{
		DebugLogging:                false,
		EnhancedMetrics:             true,
		DDTraceEnabled:              true,
		MergeXrayTraces:             false,
		CircuitBreakerInterval:      0,
		CircuitBreakerTimeout:       0,
		CircuitBreakerTotalFailures: 0,
	}
}
