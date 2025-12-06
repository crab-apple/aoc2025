class Operation:

    def __init__(self, operands, operator):
        self._operands = operands
        self._operator = operator

    def __eq__(self, other):
        return other._operands == self._operands and other._operator == self._operator

    def __repr__(self):
        return "Operation({}, '{}')".format(self._operands, self._operator)
