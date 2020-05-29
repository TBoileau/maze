import random
from typing import List, Tuple

from src.domain.entity.case import Case
from src.domain.entity.end import End
from src.domain.entity.maze import Maze
from src.domain.entity.start import Start
from src.domain.entity.wall import Wall
from src.domain.presenter.create_maze_presenter \
    import CreateMazePresenterInterface
from src.domain.request.create_maze_request import CreateMazeRequest
from src.domain.response.create_maze_response import CreateMazeResponse


class CreateMaze:
    def execute(
            self,
            request: CreateMazeRequest,
            presenter: CreateMazePresenterInterface
    ):
        maze: Maze = Maze(request.x, request.y)

        x = 2 * maze.x + 1
        y = 2 * maze.y + 1
        rows: List[List[int]] = [[0 for i in range(x)] for j in range(y)]
        (rx, ry) = (
            2 * random.randrange(maze.x) + 1,
            2 * random.randrange(maze.y) + 1
        )
        rows[ry][rx] = 1
        directions = (
            {
                "up": 0,
                "down": 0,
                "right": 2,
                "left": -2
            },
            {
                "up": -2,
                "down": 2,
                "right": 0,
                "left": 0
            }
        )
        temp_cells: List[Tuple[int, int]] = []

        for direction in ["up", "down", "right", "left"]:
            (nx, ny) = (
                rx + directions[0][direction],
                ry + directions[1][direction]
            )
            if 0 <= nx < x and 0 <= ny < y:
                rows[ny][nx] = 2
                temp_cells.append((nx, ny))

        while temp_cells:
            (rx, ry) = random.choice(temp_cells)
            temp_cells.remove((rx, ry))
            rows[ry][rx] = 1
            neighbours: List[Tuple[int, int]] = []
            for direction in ["up", "down", "right", "left"]:
                (nx, ny) = (
                    rx + directions[0][direction],
                    ry + directions[1][direction]
                )
                if 0 <= nx < x and 0 <= ny < y and rows[ny][nx] == 1:
                    neighbours.append((nx, ny))
            for direction in ["up", "down", "right", "left"]:
                (nx, ny) = (
                    rx + directions[0][direction],
                    ry + directions[1][direction]
                )
                if 0 <= nx < x and 0 <= ny < y and rows[ny][nx] == 0:
                    rows[ny][nx] = 2
                    temp_cells.append((nx, ny))
            if len(neighbours) > 0:
                (nx, ny) = random.choice(neighbours)
                rows[int((ny + ry) / 2)][int((nx + rx) / 2)] = 1
                rows[ny][nx] = 1
        (sx, sy) = (0, 2 * random.randrange(maze.y) + 1)
        (ex, ey) = (2 * maze.x, 2 * random.randrange(maze.y) + 1)
        rows[sy][sx] = 2
        rows[ey][ex] = 3

        for y in range(len(rows)):
            for x in range(len(rows[y])):
                if rows[y][x] == 0:
                    maze.add(Wall(x, y))
                if rows[y][x] == 1:
                    maze.add(Case(x, y))
                if rows[y][x] == 2:
                    maze.add(Start(x, y))
                if rows[y][x] == 3:
                    maze.add(End(x, y))

        presenter.present(CreateMazeResponse(maze))
