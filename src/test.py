import Sym
import Num
from utils import oo
# import oo
def test_sym():
    
    sym = Sym.Sym()
    pairs = ["a", "a", "a", "b", "b", "c"]
    for x in pairs:
        sym.add(x)
    mode = sym.mid()
    entropy = sym.div()
    entropy = 1000*entropy // 1/ 1000

    return mode == "a" and  1.37 <= entropy and entropy <= 1.38 

def test_num():
    num = Num.Num()
    for i in range(1, 1000):
        num.add(i)
    mid = num.mid()
    div = num.div()

    print (mid, div)
    return 50<= mid and mid<= 52 and 30.5 <div and div<32

def bignum():
    num = Num.Num()
    num.nums_max = 32
    for i in range(1, 1000):
        num.add(i)
    import pdb; pdb.set_trace()
    oo(num.nums())
    return 32==len(num.has)

bignum()

    
