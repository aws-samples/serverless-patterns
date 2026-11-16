/* Sticky Notes Board — web UI
 *
 * The browser talks ONLY to the middleware (API Gateway). It never contacts
 * the MicroVM endpoint directly — that endpoint has no browser-usable CORS and
 * requires an auth token we deliberately keep server-side.
 *
 * Flow:
 *   1. User gives the middleware API Gateway URL + a clientId.
 *   2. POST {middleware}/session  -> { restored, reused, ... }
 *      The middleware reuses a live MicroVM or launches a fresh one (restoring
 *      the client's notes + files from S3 via the /run hook).
 *   3. All note/file calls go to the middleware proxy:
 *        {middleware}/api/notes, {middleware}/api/files, ...
 *      with header  X-Client-Id: {clientId}.  The middleware injects the
 *      MicroVM auth token and forwards the request.
 */

const COLORS = ["yellow", "blue", "green", "red", "purple", "orange"];
const LS_KEY = "stickynotes.session";

const session = {
  middlewareUrl: "",
  clientId: "",
};

/* ---------- small DOM helpers ---------- */
const $ = (sel) => document.querySelector(sel);
const el = (tag, cls, html) => {
  const n = document.createElement(tag);
  if (cls) n.className = cls;
  if (html != null) n.innerHTML = html;
  return n;
};

function toast(msg, kind = "") {
  const t = $("#toast");
  t.textContent = msg;
  t.className = "toast " + kind;
  t.hidden = false;
  clearTimeout(toast._t);
  toast._t = setTimeout(() => (t.hidden = true), 3200);
}

function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, (c) =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c])
  );
}

function fmtSize(bytes) {
  if (bytes < 1024) return bytes + " B";
  if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + " KB";
  return (bytes / (1024 * 1024)).toFixed(1) + " MB";
}

/* ---------- API layer ---------- */
// All app requests go through the middleware proxy at {middlewareUrl}/api/...
// identified by the X-Client-Id header. The middleware adds the MicroVM token.
async function api(path, opts = {}) {
  const headers = Object.assign(
    { "X-Client-Id": session.clientId },
    opts.headers || {}
  );
  const url = `${session.middlewareUrl}/api${path}`;
  const res = await fetch(url, { ...opts, headers });
  if (!res.ok) {
    let detail = "";
    try { detail = (await res.json()).error || ""; } catch (_) {}
    throw new Error(`${res.status} ${detail}`.trim());
  }
  return res;
}
const apiJson = async (path, opts) => (await api(path, opts)).json();

/* ---------- session / connect ---------- */
async function openSession(middlewareUrl, clientId) {
  const base = middlewareUrl.replace(/\/+$/, "");
  const res = await fetch(base + "/session", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ clientId }),
  });
  if (!res.ok) {
    let detail = "";
    try { detail = (await res.json()).error || ""; } catch (_) {}
    throw new Error(`Middleware error ${res.status} ${detail}`.trim());
  }
  const data = await res.json();
  session.middlewareUrl = base;
  session.clientId = clientId;
  localStorage.setItem(
    LS_KEY,
    JSON.stringify({ middlewareUrl: base, clientId })
  );
  return data;
}

async function connect() {
  const url = $("#middleware-url").value.trim();
  const cid = $("#client-id").value.trim();
  const status = $("#connect-status");
  if (!url || !cid) {
    status.hidden = false;
    status.className = "connect-status error";
    status.textContent = "Both fields are required.";
    return;
  }
  const btn = $("#connect-btn");
  btn.disabled = true;
  btn.textContent = "Starting workspace…";
  status.hidden = false;
  status.className = "connect-status";
  status.textContent = "Contacting middleware (this may launch a MicroVM)…";
  try {
    const data = await openSession(url, cid);
    status.className = "connect-status ok";
    const how = data.reused
      ? "Reconnected to your running MicroVM."
      : data.restored
      ? "Launched a fresh MicroVM and restored your last session."
      : "Launched a new MicroVM.";
    status.textContent = how;
    enterWorkspace(data);
  } catch (e) {
    status.className = "connect-status error";
    status.textContent = e.message || "Failed to open session.";
  } finally {
    btn.disabled = false;
    btn.textContent = "Open my workspace";
  }
}

function enterWorkspace(data) {
  $("#connect-screen").hidden = true;
  $("#workspace").hidden = false;
  $("#client-label").textContent = session.clientId;

  // Show the MicroVM id in the top bar (full value available on hover).
  const mvmItem = $("#microvm-item");
  const mvmLabel = $("#microvm-label");
  if (data.microvmId) {
    session.microvmId = data.microvmId;
    mvmLabel.textContent = data.microvmId;
    mvmLabel.title = data.microvmId;
    mvmItem.hidden = false;
  } else {
    mvmItem.hidden = true;
  }

  const pill = $("#session-pill");
  if (data.reused) { pill.textContent = "reused session"; pill.className = "pill reused"; }
  else if (data.restored) { pill.textContent = "restored from S3"; pill.className = "pill restored"; }
  else { pill.textContent = "new session"; pill.className = "pill"; }
  refreshAll();
}

function disconnect() {
  // Tell the middleware the UI closed (keeps the record for next restore).
  if (session.middlewareUrl && session.clientId) {
    fetch(session.middlewareUrl + "/session/close", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ clientId: session.clientId }),
      keepalive: true,
    }).catch(() => {});
  }
  $("#workspace").hidden = true;
  $("#connect-screen").hidden = false;
}

/* ---------- notes ---------- */
let notesCache = [];

async function loadNotes() {
  const data = await apiJson("/notes");
  notesCache = data.notes || [];
  renderNotes();
}

function renderNotes() {
  const grid = $("#notes-grid");
  grid.innerHTML = "";
  $("#note-count").textContent = notesCache.length;
  $("#notes-empty").hidden = notesCache.length > 0;
  for (const note of notesCache) {
    const card = el("div", "note");
    card.dataset.color = note.color || "yellow";
    card.dataset.id = note.id;
    card.innerHTML = `
      <div class="note-body">${escapeHtml(note.content)}</div>
      <div class="note-meta">#${note.id} · (${note.position_x}, ${note.position_y})</div>`;
    card.addEventListener("click", () => openNoteModal(note));
    grid.appendChild(card);
  }
}

/* note modal */
let editingNoteId = null;
let selectedColor = "yellow";

function buildSwatches() {
  const wrap = $("#color-swatches");
  wrap.innerHTML = "";
  for (const c of COLORS) {
    const sw = el("div", "swatch");
    sw.style.background = `var(--note-${c})`;
    sw.dataset.color = c;
    sw.addEventListener("click", () => {
      selectedColor = c;
      wrap.querySelectorAll(".swatch").forEach((s) =>
        s.classList.toggle("selected", s.dataset.color === c)
      );
    });
    wrap.appendChild(sw);
  }
}

function setColorSelection(c) {
  selectedColor = c;
  $("#color-swatches").querySelectorAll(".swatch").forEach((s) =>
    s.classList.toggle("selected", s.dataset.color === c)
  );
}

function openNoteModal(note) {
  editingNoteId = note ? note.id : null;
  $("#note-modal-title").textContent = note ? "Edit note" : "New note";
  $("#note-content").value = note ? note.content : "";
  $("#note-x").value = note ? note.position_x : 0;
  $("#note-y").value = note ? note.position_y : 0;
  setColorSelection(note ? note.color || "yellow" : "yellow");
  $("#note-delete-btn").hidden = !note;
  showModal("note-modal");
}

async function saveNote() {
  const content = $("#note-content").value.trim();
  if (!content) { toast("Content is required", "error"); return; }
  const payload = {
    content,
    color: selectedColor,
    position_x: parseInt($("#note-x").value || "0", 10),
    position_y: parseInt($("#note-y").value || "0", 10),
  };
  try {
    if (editingNoteId) {
      await api(`/notes/${editingNoteId}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      toast("Note updated", "ok");
    } else {
      await api("/notes", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      toast("Note created", "ok");
    }
    hideModal("note-modal");
    await loadNotes();
  } catch (e) {
    toast("Save failed: " + e.message, "error");
  }
}

async function deleteNote() {
  if (!editingNoteId) return;
  if (!confirm("Delete this note?")) return;
  try {
    await api(`/notes/${editingNoteId}`, { method: "DELETE" });
    toast("Note deleted", "ok");
    hideModal("note-modal");
    await loadNotes();
  } catch (e) {
    toast("Delete failed: " + e.message, "error");
  }
}

/* ---------- files ---------- */
let filesCache = [];

async function loadFiles() {
  const data = await apiJson("/files");
  filesCache = data.files || [];
  renderFiles();
}

function fileIcon(f) {
  if (f.is_text) return "📝";
  if (/\.(png|jpe?g|gif|webp|svg|bmp)$/i.test(f.name)) return "🖼️";
  if (/\.(zip|tar|gz|rar|7z)$/i.test(f.name)) return "🗜️";
  if (/\.(pdf)$/i.test(f.name)) return "📕";
  return "📄";
}

function renderFiles() {
  const list = $("#files-list");
  list.innerHTML = "";
  $("#file-count").textContent = filesCache.length;
  $("#files-empty").hidden = filesCache.length > 0;
  for (const f of filesCache) {
    const row = el("li", "file-row");
    row.innerHTML = `
      <div class="file-icon">${fileIcon(f)}</div>
      <div class="file-info">
        <div class="file-name">${escapeHtml(f.name)}
          ${f.is_text ? '<span class="badge-text">text</span>' : ""}</div>
        <div class="file-sub">${fmtSize(f.size)} · ${escapeHtml(f.content_type)}</div>
      </div>`;
    const actions = el("div", "");
    actions.style.display = "flex";
    actions.style.gap = "8px";
    if (f.is_text) {
      const edit = el("button", "btn btn-ghost", "Edit");
      edit.addEventListener("click", () => openTextEditor(f.name));
      actions.appendChild(edit);
    }
    const dl = el("button", "btn btn-ghost", "Download");
    dl.addEventListener("click", () => downloadFile(f.name));
    actions.appendChild(dl);
    const del = el("button", "btn btn-danger", "Delete");
    del.addEventListener("click", () => deleteFile(f.name));
    actions.appendChild(del);
    row.appendChild(actions);
    list.appendChild(row);
  }
}

async function uploadFile(file) {
  if (!file) return;
  try {
    await api("/files", {
      method: "POST",
      headers: {
        "X-File-Name": file.name,
        "Content-Type": file.type || "application/octet-stream",
      },
      body: file,
    });
    toast(`Uploaded ${file.name}`, "ok");
    await loadFiles();
  } catch (e) {
    toast("Upload failed: " + e.message, "error");
  }
}

async function downloadFile(name) {
  try {
    const res = await api(`/files/${encodeURIComponent(name)}`);
    const blob = await res.blob();
    const url = URL.createObjectURL(blob);
    const a = el("a");
    a.href = url;
    a.download = name;
    document.body.appendChild(a);
    a.click();
    a.remove();
    URL.revokeObjectURL(url);
  } catch (e) {
    toast("Download failed: " + e.message, "error");
  }
}

async function deleteFile(name) {
  if (!confirm(`Delete "${name}"?`)) return;
  try {
    await api(`/files/${encodeURIComponent(name)}`, { method: "DELETE" });
    toast("File deleted", "ok");
    await loadFiles();
  } catch (e) {
    toast("Delete failed: " + e.message, "error");
  }
}

/* text editor modal */
let editingFileName = null;

async function openTextEditor(name) {
  try {
    const data = await apiJson(`/files/${encodeURIComponent(name)}/text`);
    editingFileName = name;
    $("#text-modal-title").textContent = `Edit · ${name}`;
    $("#text-editor").value = data.content;
    $("#text-status").textContent = "";
    showModal("text-modal");
  } catch (e) {
    toast("Can't open file: " + e.message, "error");
  }
}

async function saveTextFile() {
  if (!editingFileName) return;
  const btn = $("#text-save-btn");
  btn.disabled = true;
  try {
    await api(`/files/${encodeURIComponent(editingFileName)}/text`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ content: $("#text-editor").value }),
    });
    $("#text-status").textContent = "Saved ✓";
    toast("File saved", "ok");
    await loadFiles();
  } catch (e) {
    toast("Save failed: " + e.message, "error");
  } finally {
    btn.disabled = false;
  }
}

/* ---------- shared ---------- */
// After a MicroVM boots (or resumes), the /run hook restores notes + files
// from S3 in a background thread. Until it finishes, the app answers /notes
// and /files with 503 "Board not initialized". So on load we poll, retrying
// specifically on 503, until the board is ready or we exhaust the budget.
async function refreshAll({ retries = 20, delayMs = 1500 } = {}) {
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  for (let attempt = 1; attempt <= retries; attempt++) {
    try {
      await Promise.all([loadNotes(), loadFiles()]);
      return; // success
    } catch (e) {
      const booting = String(e.message).startsWith("503");
      if (!booting || attempt === retries) {
        toast("Could not load workspace: " + e.message, "error");
        return;
      }
      if (attempt === 1) toast("Workspace is waking up…", "");
      await sleep(delayMs);
    }
  }
}

function showModal(id) { $("#" + id).hidden = false; }
function hideModal(id) { $("#" + id).hidden = true; }

/* ---------- wire up ---------- */
function init() {
  buildSwatches();

  // Restore last-used middleware URL + clientId for convenience.
  try {
    const saved = JSON.parse(localStorage.getItem(LS_KEY) || "{}");
    if (saved.middlewareUrl) $("#middleware-url").value = saved.middlewareUrl;
    if (saved.clientId) $("#client-id").value = saved.clientId;
  } catch (_) {}

  $("#connect-btn").addEventListener("click", connect);
  $("#client-id").addEventListener("keydown", (e) => { if (e.key === "Enter") connect(); });
  $("#disconnect-btn").addEventListener("click", disconnect);
  $("#refresh-btn").addEventListener("click", refreshAll);

  $("#new-note-btn").addEventListener("click", () => openNoteModal(null));
  $("#note-save-btn").addEventListener("click", saveNote);
  $("#note-delete-btn").addEventListener("click", deleteNote);

  $("#upload-btn").addEventListener("click", () => $("#file-input").click());
  $("#file-input").addEventListener("change", (e) => {
    if (e.target.files[0]) uploadFile(e.target.files[0]);
    e.target.value = "";
  });
  $("#text-save-btn").addEventListener("click", saveTextFile);

  // drag & drop upload
  const dz = $("#dropzone");
  ["dragenter", "dragover"].forEach((ev) =>
    dz.addEventListener(ev, (e) => { e.preventDefault(); dz.classList.add("drag"); })
  );
  ["dragleave", "drop"].forEach((ev) =>
    dz.addEventListener(ev, (e) => { e.preventDefault(); dz.classList.remove("drag"); })
  );
  dz.addEventListener("drop", (e) => {
    const f = e.dataTransfer.files[0];
    if (f) uploadFile(f);
  });

  // modal close buttons + backdrop click
  document.querySelectorAll("[data-close]").forEach((b) =>
    b.addEventListener("click", () => hideModal(b.dataset.close))
  );
  document.querySelectorAll(".modal").forEach((m) =>
    m.addEventListener("click", (e) => { if (e.target === m) m.hidden = true; })
  );
}

document.addEventListener("DOMContentLoaded", init);
