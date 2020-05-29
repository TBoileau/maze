from src.domain.entity.maze import Maze


class CreateMazeResponse():
    def __init__(self, maze: Maze):
        self.maze: Maze = maze
