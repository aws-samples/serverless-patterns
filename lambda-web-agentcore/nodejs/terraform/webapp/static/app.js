$(function () {
  const $messages = $("#messages");
  const $emptyState = $("#empty-state");
  const $composer = $("#composer");
  const $prompt = $("#prompt");
  const $send = $("#send");
  const $stop = $("#stop");

  let abortController = null;

  // One AgentCore session per browser tab, so users never share an agent session.
  const sessionId = sessionStorage.getItem("sessionId") ?? crypto.randomUUID();
  sessionStorage.setItem("sessionId", sessionId);

  function addMessage(role) {
    const $message = $("<div>").addClass(`message ${role}`).append($("<div>").addClass("content"));
    $emptyState.hide();
    $messages.append($message);
    scrollToBottom();
    return $message;
  }

  function scrollToBottom() {
    $messages.scrollTop($messages.prop("scrollHeight"));
  }

  function renderMarkdown(text) {
    return DOMPurify.sanitize(marked.parse(text));
  }

  function setStreaming(streaming) {
    $send.prop("hidden", streaming);
    $stop.prop("hidden", !streaming);
    $prompt.prop("disabled", streaming);
  }

  function updateSendButton() {
    $send.prop("disabled", $prompt.val().trim() === "");
  }

  // Parse an SSE byte stream into JSON events ("data: {...}\n\n" frames).
  async function* readSseEvents(body) {
    const reader = body.pipeThrough(new TextDecoderStream()).getReader();
    let buffer = "";
    while (true) {
      const { value, done } = await reader.read();
      if (done) return;
      buffer += value;
      let boundary;
      while ((boundary = buffer.indexOf("\n\n")) !== -1) {
        const frame = buffer.slice(0, boundary);
        buffer = buffer.slice(boundary + 2);
        const data = frame
          .split("\n")
          .filter((line) => line.startsWith("data:"))
          .map((line) => line.slice(5).trimStart())
          .join("\n");
        if (data) yield JSON.parse(data);
      }
    }
  }

  async function sendPrompt(prompt) {
    addMessage("user").find(".content").text(prompt);
    const $assistant = addMessage("assistant");
    const $content = $assistant.find(".content").addClass("typing-indicator");

    let text = "";
    abortController = new AbortController();
    setStreaming(true);

    try {
      const response = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt, sessionId }),
        signal: abortController.signal,
      });
      if (!response.ok) {
        const body = await response.json().catch(() => ({}));
        throw new Error(body.error ?? `Request failed with status ${response.status}`);
      }

      for await (const event of readSseEvents(response.body)) {
        if (event.type === "chunk") {
          text += event.data;
          $content.removeClass("typing-indicator").html(renderMarkdown(text));
          scrollToBottom();
        } else if (event.type === "error" || event.error) {
          throw new Error(event.error ?? event.message ?? "Agent error");
        }
      }
    } catch (err) {
      if (err.name !== "AbortError") {
        $assistant.addClass("error");
        $content.append($("<p>").text(`Error: ${err.message}`));
      }
    } finally {
      $content.removeClass("typing-indicator");
      abortController = null;
      setStreaming(false);
      $prompt.trigger("focus");
      scrollToBottom();
    }
  }

  $composer.on("submit", (e) => {
    e.preventDefault();
    const prompt = $prompt.val().trim();
    if (!prompt || abortController) return;
    $prompt.val("").trigger("input");
    sendPrompt(prompt);
  });

  // Enter sends, Shift+Enter inserts a newline.
  $prompt.on("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey && !e.originalEvent.isComposing) {
      e.preventDefault();
      $composer.trigger("submit");
    }
  });

  // Grow the textarea with its content.
  $prompt.on("input", function () {
    this.style.height = "auto";
    this.style.height = `${this.scrollHeight}px`;
    updateSendButton();
  });

  $stop.on("click", () => abortController?.abort());

  updateSendButton();
});
