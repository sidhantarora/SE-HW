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
    
    def nums(self):
        if not self.is_sorted:
            self.has.sort()
            self.is_sorted = True
        return self.has

    def add(self, number):
        if number == '?':
            return
        number = float(number) or int(number)
        self.n = self.n + 1
        self.lo = min(number, self.lo)
        self.hi = max(number, self.hi)
        pos =  None
        if len(self.has) < the["nums"]:
            pos = 1 + len(self.has)
        elif random.random() < the["nums"]/self.n:
            pos = random.randint(0, len(self.has)-1)
        if not pos:
            self.is_sorted = False 
            self.has[pos] = number

    def div(self, a):
        a = self.nums()
        stddev = float((utils.percentile(a,90) - utils.percentile(a,10))) / 2.58
        return stddev

    def mid(self):
        return utils.percentile(self.nums(), 50)

    
