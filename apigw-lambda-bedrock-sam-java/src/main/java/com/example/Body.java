package com.example;

import org.json.JSONObject;

import java.text.MessageFormat;


    record Body(String prompt, double temperature, int top_k, double top_p, int max_tokens) {

    public static final String PROMPT_TEMPLATE = "\\n\n[INST] {0} \\n\\n[/INST]";

    Body(String promptContent) {
        this(MessageFormat.format(PROMPT_TEMPLATE, promptContent),
                0.5,
                50,
                0.7,
                400);
    }

    String toJson() {
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("prompt", prompt);
        jsonObject.put("temperature", temperature);
        jsonObject.put("top_k", top_k);
        jsonObject.put("top_p", top_p);
        jsonObject.put("max_tokens", max_tokens);

        return jsonObject.toString();
    }
}
