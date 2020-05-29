class CreateMazeRequest:
    def __init__(self, x: int, y: int):
        assert x > 2
        assert y > 2
        self.x: int = x
        self.y: int = y
