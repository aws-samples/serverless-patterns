// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

package com.unicorn.store.data;

import com.unicorn.store.model.Unicorn;
import software.amazon.awssdk.services.dynamodb.model.AttributeValue;

import java.util.HashMap;
import java.util.Map;

public class UnicornMapper {
    private static final String PK = "PK";
    private static final String NAME = "name";
    private static final String AGE = "age";
    private static final String SIZE = "size";
    private static final String TYPE = "type";

    public static Unicorn unicornFromDynamoDB(Map<String, AttributeValue> item) {
        Unicorn unicorn = new Unicorn();
        unicorn.setId(item.get(PK).s());
        unicorn.setType(item.get(TYPE).s());
        unicorn.setSize(item.get(SIZE).s());
        unicorn.setName(item.get(NAME).s());
        unicorn.setAge(item.get(AGE).s());

        return unicorn;
    }

    public static Map<String, AttributeValue> unicornToDynamoDB(Unicorn unicorn) {
        Map<String, AttributeValue> item = new HashMap<>();
        item.put(PK, AttributeValue.builder().s(unicorn.getId()).build());
        item.put(NAME, AttributeValue.builder().s(unicorn.getName()).build());
        item.put(AGE, AttributeValue.builder().s(unicorn.getAge()).build());
        item.put(SIZE, AttributeValue.builder().s(unicorn.getSize()).build());
        item.put(TYPE, AttributeValue.builder().s(unicorn.getType()).build());

        return item;
    }
}
