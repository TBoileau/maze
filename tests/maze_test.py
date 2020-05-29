from src.domain.entity.maze import Maze
from src.domain.presenter.create_maze_presenter \
    import CreateMazePresenterInterface
from src.domain.request.create_maze_request import CreateMazeRequest
from src.domain.response.create_maze_response import CreateMazeResponse
from src.domain.use_case.create_maze import CreateMaze


class CreateMazePresenter(CreateMazePresenterInterface):
    response: CreateMazeResponse

    def present(self, response: CreateMazeResponse):
        self.response = response


def test_if_maze_is_created():
    create_maze_request: CreateMazeRequest = CreateMazeRequest(5, 5)
    create_maze_presenter: CreateMazePresenter = CreateMazePresenter()
    create_maze: CreateMaze = CreateMaze()
    create_maze.execute(create_maze_request, create_maze_presenter)
    assert isinstance(create_maze_presenter.response.maze, Maze)
    assert 121 == len(create_maze_presenter.response.maze.cells)
