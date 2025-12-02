class Dial:

    def __init__(self):
        self._pointer = 0

    def pointer(self):
        return self._pointer

    def rotate(self, direction, steps):

        if direction == "R":
            pass
        elif direction == "L":
            steps = -steps
        elif type(direction) is str:
            raise ValueError("Invalid value: " + direction)
        else:
            raise TypeError("Invalid type: " + type(direction))

        self._pointer += steps

        self._pointer %= 100
