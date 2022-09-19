from . import Num
from . import Sym
import re

class Cols:
    def __init__(self, names):
        self.names = names
        self.all = []
        self.klass = None
        self.x = []
        self.x_names = []
        self.eligible = []
        self.y = []
        self.y_names = []
        self.skipped_items = []
        key = 0
        self.eligible_names = []
        
        for key in names:
            obj = {}
            col_name = names[key]
            if re.match("^[A-Z]",col_name):
                obj = Num.Num(key,col_name)
                self.all.append(obj)
            else:
                obj = Sym.Sym(key,col_name)
                self.all.append(obj)
            
            if not col_name.endswith(":"):
                is_dependent = col_name.endswith("+") or col_name.endswith("-")
                if is_dependent:
                    self.y.append(obj)
                    self.y_names.append(col_name)
                else:
                    self.x.append(obj)
                    self.x_names.append(col_name)
                if col_name.endswith("!"):
                    self.klass = obj
                self.eligible.append(obj)
                self.eligible_names.append(col_name)
            else:
                self.eligible.append(None)
            key+=1