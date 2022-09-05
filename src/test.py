import Sym
import Num
from utils import oo
# import oo
def test_sym():
    
    sym = Sym.Sym()
    pairs = ["a", "a", "a", "a", "b", "b", "c"]
    for x in pairs:
        sym.add(x)
    mode = sym.mid()
    entropy = sym.div()
    entropy = 1000*entropy // 1/ 1000

    return mode == "a" and  1.37 <= entropy and entropy <= 1.38 

def test_num():
    num = Num.Num()
    for i in range(1, 100):
        num.add(i)
    mid = num.mid()
    div = num.div()

    # print (mid, div)
    return 50<= mid and mid<= 52 and 30.5 <div and div<32

def bignum():
    num = Num.Num()
    num.nums_max = 32
    for i in range(1, 1000):
        num.add(i)
    # import pdb; pdb.set_trace()
    oo(num.nums())
    # print(len(num.has))
    return 32==len(num.has)

def run_tests():
    test_case_num =1 
    val = bignum()
    if val: print("TestCase "+str(test_case_num)+" Passed")
    else: print("TestCase "+str(test_case_num)+" Failed")
    test_case_num+=1
    val = test_num()
    if val: print("TestCase "+str(test_case_num)+" Passed")
    else: print("TestCase "+str(test_case_num)+" Failed")
    test_case_num+=1
    val = test_sym()
    if val: print("TestCase "+str(test_case_num)+" Passed")
    else: print("TestCase "+str(test_case_num)+" Failed")


if __name__=="__main__":
    run_tests()


    
