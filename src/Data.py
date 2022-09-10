import csv
import Cols

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