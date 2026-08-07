package com.amazonaws.samples.durable.models;

import java.util.List;
import java.util.Map;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;

public class SnsEventParser {

    private static final ObjectMapper mapper = new ObjectMapper();

    @SuppressWarnings("unchecked")
    public static Map<String, Object> extractMessage(Map<String, Object> event) {
        try {
            List<Map<String, Object>> records = (List<Map<String, Object>>) event.get("Records");
            if (records != null && !records.isEmpty()) {
                Map<String, Object> sns = (Map<String, Object>) records.get(0).get("Sns");
                String message = (String) sns.get("Message");
                return mapper.readValue(message, new TypeReference<Map<String, Object>>() {});
            }
        } catch (Exception e) {
            // Not an SNS event envelope, return as-is
        }
        return event;
    }
}
