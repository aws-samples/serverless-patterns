package lib

import (
	log "github.com/sirupsen/logrus"
)

func SetLevel(level string) {
	//	_ = os.Setenv("LOG_LEVEL", "debug")
	switch level {
	case "error":
		log.SetLevel(log.ErrorLevel)
	case "info":
		log.SetLevel(log.InfoLevel)
	case "debug":
		log.SetLevel(log.DebugLevel)
	case "trace":
		log.SetLevel(log.TraceLevel)
	default:
		log.SetLevel(log.DebugLevel)
	}
}
