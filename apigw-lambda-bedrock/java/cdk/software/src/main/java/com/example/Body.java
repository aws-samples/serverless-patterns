package com.example;

import org.json.JSONObject;

import java.text.MessageFormat;


record Body(String prompt, double temperature, int top_k, double top_p, int max_tokens_to_sample,
            String[] stop_sequences, String anthropic_version) {


    public static final String PROMPT_TEMPLATE = "Human: {0} \\n\\nAssistant:";


    Body(String promptContent) {
        this(MessageFormat.format(PROMPT_TEMPLATE, promptContent),
                0.5,
                250,
                0.999,
                300,
                new String[]{"\\n\\nHuman:"},
                "bedrock-2023-05-31");
    }

    String toJson() {
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("prompt", prompt);
        jsonObject.put("temperature", temperature);
        jsonObject.put("top_k", top_k);
        jsonObject.put("top_p", top_p);
        jsonObject.put("max_tokens_to_sample", max_tokens_to_sample);
        jsonObject.put("stop_sequences", stop_sequences);
        jsonObject.put("anthropic_version", anthropic_version);

        return jsonObject.toString();
    }
}
