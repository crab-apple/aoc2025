class InvalidId:
    def __init__(self, base, repeats):
        self._base = base
        self._repeats = repeats

    def as_int(self):
        return int(str(self._base) * self._repeats)

    def next(self):
        return InvalidId(self._base + 1, self._repeats)

    def prev(self):
        if self._base == 1:
            return None
        return InvalidId(self._base - 1, self._repeats)
