from typing import List

from src.domain.entity.cell import Cell


class Maze:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y
        self.cells: List[Cell] = []

    def add(self, cell: Cell):
        self.cells.append(cell)
