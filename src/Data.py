import csv
import Cols
import rnd

class Data:
    def __init__(self, src) -> None:
        self.cols = None
        self.rows = []

        if type(src) == type("xyz"):
            csv(src, lambda row : self.add(row))
        else:
            for row in src:
                self.add(row)
    
    def add(self, row):
        if not self.cols:
            self.cols = Cols(row)
        for todo in self.cols.data:
            for col in todo:
                col.add(row.cells[col.at])

    def stats(self, places, showCols, func):
        sc = None
        if showCols:
            sc = showCols
        else:
            sc = self.cols.y
        t = dict()
        x = False
        for col in sc:
            v = func(col)
            if type(v) == type(1) and rnd(v, places):
                x = True
                t[col.name] = x
            else:
                t[col.name] = v
        return t
