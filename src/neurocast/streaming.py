"""Streaming ingestion helpers for Neurocast Engine."""

from collections import deque


class SlidingWindow:
    def __init__(self, size: int):
        self.size = size
        self._buffer = deque(maxlen=size)

    def push(self, value: float) -> None:
        self._buffer.append(float(value))

    def values(self):
        return list(self._buffer)

    def ready(self) -> bool:
        return len(self._buffer) == self.size
