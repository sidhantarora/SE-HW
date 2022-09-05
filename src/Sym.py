import math
class Sym:
    def __init__(self, pos=0, colName=""):
        self.n = 0
        self.pos = pos
        self.colName = colName
        self.has = {}

    def add(self, symbol):
        # import pdb; pdb.set_trace()
        if symbol == '?':
            return
        self.n = self.n + 1
        if symbol in self.has:
            self.has[symbol] = self.has[symbol] + 1
        else:
            self.has[symbol] = 1
    
    def mid(self):
        most, mode = -1, 0
        for k in self.has:
            v = self.has[k]
            if v > most:
                most = v
                mode = k
        return mode

    def div(self):
        e = 0
        for k in self.has:
            v = self.has[k]
            if v > 0:
                e = e - self.helper(v/self.n)
        return e

    def helper(self,p):
        return p * math.log(p,2)