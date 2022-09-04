import math
from operator import truediv
import sys
class Num:
    def __init__(self, pos=0, colName=""):
        self.n = 0
        self.pos = pos
        self.colName = colName
        self.has = []
        self.lo = sys.maxsize 
        self.hi = -sys.maxsize - 1
        self.is_sorted = True 
        self.w = (self.colName.find("-$") and -1 or 1)
    
    def nums(self):
        if not self.is_sorted:
            self.has.sort()
            self.is_sorted = True
        return self.has
