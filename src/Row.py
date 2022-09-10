import sys
import utils


class Row:
    def __init__(self, t):
        self.cells = t
        self.cooked = utils.copy(t)
        self.isEvaled = False