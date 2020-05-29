from abc import ABC, abstractmethod

from src.domain.response.create_maze_response import CreateMazeResponse


class CreateMazePresenterInterface(ABC):
    @abstractmethod
    def present(self, response: CreateMazeResponse):
        pass
