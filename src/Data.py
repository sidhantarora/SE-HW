import Cols
import utils
import Row

class Data:
    def __init__(self, src) -> None:
        self.cols = None
        self.rows = []
        if type(src) is str:
            utils.csv(src, lambda row : self.add(row))
        else:
            for row in src:
                self.add(row)
    
    def add(self, row):
        if not self.cols:
            self.cols = Cols.Cols(row)
        else:
            if type(row) == Row.Row:
                self.rows.append(row.cells)
            else:
                self.rows.append(Row.Row(row))
            for index in self.rows[-1].cells:
                element = self.rows[-1].cells[index]
                if self.cols.eligible[index - 1]:
                    self.cols.eligible[index - 1].add(element)
            

    def stats(self, places, showCols, func):
        # import pdb; pdb.set_trace()
        sc = None
        if showCols:
            sc = showCols
        else:
            sc = self.cols.y
        t = dict()
        x = False
        for index, col in enumerate(sc):
            v = func(col)
            if (type(v) == type(1)) and utils.rnd(v, places):
                x = True
                t[index] = x
            else:
                t[index] = v
        return t
