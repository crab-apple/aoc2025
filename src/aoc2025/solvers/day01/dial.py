class Dial:

    def __init__(self):
        self._pointer = 0

    def pointer(self):
        return self._pointer

    def rotate(self, direction, steps):

        invert = False

        if direction == "R":
            pass
        elif direction == "L":
            invert = True
        elif type(direction) is str:
            raise ValueError("Invalid value: " + direction)
        else:
            raise TypeError("Invalid type: " + type(direction))

        if invert:
            self._invert_pointer()

        self._pointer += steps

        loops = self._pointer // 100
        self._pointer %= 100

        if invert:
            self._invert_pointer()

        return loops

    def _invert_pointer(self):
        self._pointer = (100 - self._pointer) % 100
