from dataclasses import dataclass


@dataclass
class Cell:

    x: int
    y: int
    is_alive: bool

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.is_alive = False

    def resurrect(self) -> None:
        """Brings the cell back to life."""
        self.is_alive = True

    def kill(self) -> None:
        """Kills the cell."""
        self.is_alive = False
