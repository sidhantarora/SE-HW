import Sym
import Num
from utils import oo
# import oo
def test_sym():
    import pdb; pdb.set_trace()
    sym = Sym.Sym()
    pairs = ["a", "a", "a", "b", "b", "c"]
    for x in pairs:
        sym.add(x)
    mode = sym.mid
    entropy = sym.div
    entropy = 1000*entropy // 1/ 1000

    return mode == "a" and  1.37 <= entropy and entropy <= 1.38 

def test_num():
    num = Num()
    for i in range(1, 1000):
        num.add(i)
    mid = num.mid()
    div = num.div()

    print (mid, div)
    return 50<= mid and mid<= 52 and 30.5 <div and div<32

def bignum():
    num = Num()
    for i in range(1, 1000):
        num.add(i)

    num.nums = 32
    oo(num.nums())
    return 32==len(num.has)

test_sym()

    
