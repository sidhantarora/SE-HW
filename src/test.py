import Sym
import Num
from utils import oo

from utils import the

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

    print (mid, div)
    return 50<= mid and mid<= 52 and 30.5 <div and div<32

def bignum():
    num = Num.Num()
    num.nums_max = 32
    for i in range(1, 1000):
        num.add(i)
    oo(num.nums())
    return 32==len(num.has)

def test_the():
    oo(the)
    return True

def run_tests():
    test_results = []
    passed_results = 0
    print("========= Starting test suite ===========")

    test_results.append(test_sym())
    test_results.append(test_num())
    test_results.append(bignum())
    test_results.append(test_the())

    test_case_num =1 
    val = bignum()
    test_results.append(val)
    if val: print("TestCase "+str(test_case_num)+" Passed")
    else: print("TestCase "+str(test_case_num)+" Failed")

    test_case_num+=1
    val = test_num()
    test_results.append(val)
    if val: print("TestCase "+str(test_case_num)+" Passed")
    else: print("TestCase "+str(test_case_num)+" Failed")

    test_case_num+=1
    val = test_sym()
    test_results.append(val)
    if val: print("TestCase "+str(test_case_num)+" Passed")
    else: print("TestCase "+str(test_case_num)+" Failed")

    test_case_num+=1
    val = test_the()
    test_results.append(val)
    if val: print("TestCase "+str(test_case_num)+" Passed")
    else: print("TestCase "+str(test_case_num)+" Failed")

    number_of_tests = len(test_results)
    for res in test_results:
        if res:
            passed_results += 1

    pass_percentage = float(passed_results * 100 /number_of_tests)
    print("Pass percentage: " + str(pass_percentage) + "%")

    print("========= Test Suite ended ===========")


if __name__=="__main__":
    run_tests()



    
