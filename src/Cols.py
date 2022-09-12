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

        import pdb; pdb.set_trace()

        key = 0
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
                else:
                    self.x.append(obj)
                if col_name.endswith("!"):
                    self.klass = obj
            key+=1
        # import pdb; pdb.set_trace()
