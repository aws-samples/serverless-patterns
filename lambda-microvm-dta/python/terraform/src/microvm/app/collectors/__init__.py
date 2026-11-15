"""Collectors observe the target from outside the target process.

Each collector implements the :class:`Collector` protocol and emits normalized
events into a shared :class:`~app.events.EventSink`. Collectors are started
before the target launches and stopped after it terminates.
"""
from __future__ import annotations

from .base import Collector, CollectorStatus

__all__ = ["Collector", "CollectorStatus"]
