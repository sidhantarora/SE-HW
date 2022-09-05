import math
from operator import truediv
import sys
import random
import utils

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
        self.nums_max = 10000000000000000000000000000
    
    def nums(self):
        if not self.is_sorted:
            self.has.sort()
            self.is_sorted = True
        return self.has

    def add(self, number):
        # import pdb; pdb.set_trace()
        if number == '?':
            return
        number = float(number) or int(number)
        self.n = self.n + 1
        self.lo = min(number, self.lo)
        self.hi = max(number, self.hi)
        pos =  -1
        x = random.random()
        if len(self.has) < self.nums_max:
            self.has.append(number)
            self.has.sort()
        elif x < self.nums_max/self.n:
            pos = random.randint(0, len(self.has)-1)

        if pos != -1:
            self.is_sorted = False 
            self.has[pos] = number

    def div(self):
        a = self.nums()
        stddev = float((utils.per(a,90) - utils.per(a,10))) / 2.58
        return stddev

    def mid(self):
        return utils.per(self.nums(), 50)

    
