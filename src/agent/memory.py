"""
DAL Context Memory — Stores and retrieves the project's DAL level.
"""


class DALMemory:
    """
    Simple memory module that persists the DAL level
    across all queries within a session.
    """

    def __init__(self):
        self._dal_level: str | None = None

    def set_dal(self, dal_level: str) -> None:
        """Store the DAL level in memory."""
        self._dal_level = dal_level

    def get_dal(self) -> str | None:
        """Retrieve the current DAL level."""
        return self._dal_level

    def reset(self) -> None:
        """Clear the DAL context."""
        self._dal_level = None

    def __repr__(self) -> str:
        return f"DALMemory(current_dal={self._dal_level})"
