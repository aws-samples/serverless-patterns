$(function () {
  const $login = $("#login");
  const $loginForm = $("#login-form");
  const $secret = $("#secret");
  const $loginButton = $("#login-button");
  const $loginError = $("#login-error");
  const $messages = $("#messages");
  const $emptyState = $("#empty-state");
  const $composer = $("#composer");
  const $prompt = $("#prompt");
  const $send = $("#send");
  const $stop = $("#stop");

  const MAX_PROMPT_LENGTH = 100;
  let abortController = null;

  // The signed session token from /connect. It is kept only in memory, so a reload shows the
  // login screen again and starts a new conversation.
  let sessionToken = null;

  async function connect(secret) {
    const response = await fetch("/connect", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ secret }),
    });
    if (response.status === 401) throw new Error("Invalid login secret");
    if (!response.ok) throw new Error(`Failed to connect (status ${response.status})`);
    sessionToken = (await response.json()).sessionToken;
  }

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
    $send.prop("disabled", sessionToken === null || $prompt.val().trim() === "");
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
        headers: { "Content-Type": "application/json", "X-Session-Token": sessionToken },
        body: JSON.stringify({ prompt }),
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
    if (!prompt || prompt.length > MAX_PROMPT_LENGTH || abortController) return;
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

  $loginForm.on("submit", async (e) => {
    e.preventDefault();
    const secret = $secret.val().trim();
    if (!secret) return;

    $loginButton.prop("disabled", true);
    $loginError.prop("hidden", true);
    try {
      await connect(secret);
      $login.hide();
      $messages.prop("hidden", false);
      $composer.prop("hidden", false);
      updateSendButton();
      $prompt.trigger("focus");
    } catch (err) {
      $loginError.text(err.message).prop("hidden", false);
      $secret.val("").trigger("focus");
    } finally {
      $loginButton.prop("disabled", false);
    }
  });

  updateSendButton();
});
