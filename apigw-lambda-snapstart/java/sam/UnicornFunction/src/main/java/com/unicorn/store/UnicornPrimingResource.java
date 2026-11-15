// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

package com.unicorn.store;

import com.unicorn.store.controller.UnicornController;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.crac.Context;
import org.crac.Core;
import org.crac.Resource;
import org.springframework.context.annotation.Configuration;

@Configuration
public class UnicornPrimingResource implements Resource {

    private static final Logger logger = LogManager.getLogger();

    private final UnicornController unicornController;

    public UnicornPrimingResource(UnicornController unicornController) {
        this.unicornController = unicornController;
        Core.getGlobalContext().register(this);
    }

    @Override
    public void beforeCheckpoint(Context<? extends Resource> context) {
        logger.info("beforeCheckpoint hook");
        try {
            unicornController.retrieveUnicorn("123");
        } catch (RuntimeException e) {
            // expected exception when unicorn doesn't exist.
        }
    }

    @Override
    public void afterRestore(Context<? extends Resource> context) {
        logger.debug("afterRestore hook");
    }
}
