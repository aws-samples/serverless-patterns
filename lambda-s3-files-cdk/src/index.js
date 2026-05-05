const fs = require("fs");
const path = require("path");

const MOUNT_PATH = process.env.MOUNT_PATH || "/mnt/s3data";

/** Resolve user input to a safe path under MOUNT_PATH. Throws on traversal. */
function safePath(userInput) {
  const resolved = path.resolve(MOUNT_PATH, userInput);
  if (!resolved.startsWith(MOUNT_PATH + path.sep) && resolved !== MOUNT_PATH) {
    throw new Error(`Path traversal blocked: ${userInput}`);
  }
  return resolved;
}

exports.handler = async (event) => {
  const action = event.action || "list";

  switch (action) {
    case "write": {
      const filename = event.filename || "hello.txt";
      const content = event.content || `Written by Lambda at ${new Date().toISOString()}`;
      const filePath = safePath(filename);
      fs.mkdirSync(path.dirname(filePath), { recursive: true });
      fs.writeFileSync(filePath, content);
      return { status: "written", path: filePath, size: Buffer.byteLength(content) };
    }

    case "read": {
      const filename = event.filename || "hello.txt";
      const filePath = safePath(filename);
      if (!fs.existsSync(filePath)) {
        return { status: "not_found", path: filePath };
      }
      const content = fs.readFileSync(filePath, "utf-8");
      return { status: "read", path: filePath, content, size: content.length };
    }

    case "list":
    default: {
      const dir = event.directory || "";
      const targetPath = safePath(dir);
      if (!fs.existsSync(targetPath)) {
        return { status: "not_found", path: targetPath };
      }
      const entries = fs.readdirSync(targetPath, { withFileTypes: true }).map((e) => ({
        name: e.name,
        type: e.isDirectory() ? "directory" : "file",
      }));
      return { status: "listed", path: targetPath, count: entries.length, entries };
    }
  }
};
