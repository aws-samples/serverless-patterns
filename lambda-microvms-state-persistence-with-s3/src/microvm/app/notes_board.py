"""
Sticky Notes Board - In-memory state that accumulates over time.
Each client gets their own isolated board identified by clientId.
"""

import uuid
from datetime import datetime, timezone
from dataclasses import dataclass, field, asdict
from typing import Optional


@dataclass
class Note:
    id: str
    content: str
    color: str
    position_x: int
    position_y: int
    created_at: str

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class Board:
    client_id: str
    notes: dict[str, Note] = field(default_factory=dict)
    created_at: str = ""
    last_modified_at: str = ""

    def __post_init__(self):
        now = datetime.now(timezone.utc).isoformat()
        if not self.created_at:
            self.created_at = now
        if not self.last_modified_at:
            self.last_modified_at = now

    def add_note(
        self,
        content: str,
        color: str = "yellow",
        position_x: int = 0,
        position_y: int = 0,
    ) -> Note:
        note_id = str(uuid.uuid4())[:8]
        note = Note(
            id=note_id,
            content=content,
            color=color,
            position_x=position_x,
            position_y=position_y,
            created_at=datetime.now(timezone.utc).isoformat(),
        )
        self.notes[note_id] = note
        self.last_modified_at = datetime.now(timezone.utc).isoformat()
        return note

    def update_note(
        self,
        note_id: str,
        content: Optional[str] = None,
        color: Optional[str] = None,
        position_x: Optional[int] = None,
        position_y: Optional[int] = None,
    ) -> Optional[Note]:
        note = self.notes.get(note_id)
        if note is None:
            return None
        if content is not None:
            note.content = content
        if color is not None:
            note.color = color
        if position_x is not None:
            note.position_x = position_x
        if position_y is not None:
            note.position_y = position_y
        self.last_modified_at = datetime.now(timezone.utc).isoformat()
        return note

    def remove_note(self, note_id: str) -> bool:
        if note_id in self.notes:
            del self.notes[note_id]
            self.last_modified_at = datetime.now(timezone.utc).isoformat()
            return True
        return False

    def get_note(self, note_id: str) -> Optional[Note]:
        return self.notes.get(note_id)

    def list_notes(self) -> list[dict]:
        return [note.to_dict() for note in self.notes.values()]

    def to_dict(self) -> dict:
        return {
            "client_id": self.client_id,
            "created_at": self.created_at,
            "last_modified_at": self.last_modified_at,
            "note_count": len(self.notes),
            "notes": self.list_notes(),
        }

    def to_serializable(self) -> dict:
        """Full state for S3 persistence."""
        return {
            "client_id": self.client_id,
            "created_at": self.created_at,
            "last_modified_at": self.last_modified_at,
            "notes": {nid: asdict(n) for nid, n in self.notes.items()},
        }

    @classmethod
    def from_serialized(cls, data: dict) -> "Board":
        """Restore board from S3-persisted data."""
        board = cls(
            client_id=data["client_id"],
            created_at=data.get("created_at", ""),
            last_modified_at=data.get("last_modified_at", ""),
        )
        for note_id, note_data in data.get("notes", {}).items():
            board.notes[note_id] = Note(**note_data)
        return board
