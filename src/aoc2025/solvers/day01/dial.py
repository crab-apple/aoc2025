class Dial:

    def __init__(self):
        self._pointer = 0

    def pointer(self):
        return self._pointer

    def rotate(self, direction, steps):

        if direction == "L":
            steps = -steps

        self._pointer += steps

        self._pointer %= 100
