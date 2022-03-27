package com.example.sqsfunction;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import com.amazonaws.services.lambda.runtime.LambdaLogger;

public class TestLogger implements LambdaLogger {
    private static final Logger logger = LoggerFactory.getLogger(TestLogger.class);

    @Override
    public void log(String s) {
        logger.info(s);
    }

    @Override
    public void log(byte[] bytes) {
        logger.info(new String(bytes));
    }
}
