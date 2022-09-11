import Num
import Sym
import re

class Cols:
    def __init__(self, names):
        self.names = names
        self.all = []
        self.klass = None
        self.x = []
        self.y = []

        for key,col_name in names:
            obj = {}
            if re.match("^[A-Z]*",col_name):
                obj = Num(key,col_name)
                self.all.append(obj)
            else:
                obj = Sym(key,col_name)
                self.all.append(obj)
            
            if not re.match(":$",col_name):
                is_dependent = re.match("[!+-]]",col_name)
                if is_dependent:
                    self.y.append(obj)
                else:
                    self.x.append(obj)
                
                if re.match("!$",col_name):
                    self.klass = obj