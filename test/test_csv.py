import os

from src import Sym, Num, Data, utils

def test_the(the):
    utils.oo(the)
    return True

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
    utils.oo(num.nums())
    return 32==len(num.has)

def func1(col):
    return col.div()

def func2(col):
    return col.mid()

def test_stats():
    path = os.path.join(os.path.dirname(__file__), '..', 'data', 'auto93.csv')
    data = Data.Data(path)
    print("xmid", data.stats(2, data.cols.x, func2))
    print("xdiv", data.stats(3, data.cols.x, func1))
    print("ymid", data.stats(2, data.cols.y, func2))
    print("ydiv", data.stats(3, data.cols.y, func1))
    return True

def test_data():
    path = os.path.join(os.path.dirname(__file__), '..', 'data', 'auto93.csv')
    data = Data.Data(path)
    for col in data.cols.y_names:
        print (col)
    return True

def func3(row):
    return

def test_csv():
    n=0
    path = os.path.join(os.path.dirname(__file__), '..', 'data', 'auto93.csv')
    utils.csv(path, func3); 
    return True

def print_test_result(test_case_num, val, func_name):
    if val: 
        print("TestCase "+str(test_case_num)+" "+func_name +" Passed")
    else: 
        print("TestCase "+str(test_case_num)+" "+func_name +" Failed")

def run_tests(the):
    test_results = []
    passed_results = 0
    print("========= Starting test suite ===========")

    test_case_num =1 
    val = bignum()
    test_results.append(val)
    
    print_test_result(test_case_num, val, "bignum")

    test_case_num+=1
    val = test_num()
    test_results.append(val)
    print_test_result(test_case_num, val, "test_num")

    test_case_num+=1
    val = test_sym()
    test_results.append(val)
    print_test_result(test_case_num, val, "test_sym")

    test_case_num+=1
    val = test_the(the)
    test_results.append(val)
    print_test_result(test_case_num, val, "test_the")


    test_case_num+=1
    try:
        val = test_stats()
        test_results.append(val)
        print_test_result(test_case_num, val, "test_stats")
    except:
        val = False
        test_results.append(val)
        print_test_result(test_case_num, val, "test_stats")

    test_case_num+=1
    val = test_data()
    test_results.append(val)
    print_test_result(test_case_num, val, "test_data")

    test_case_num+=1
    val = test_csv()
    test_results.append(val)
    print_test_result(test_case_num, val, "test_csv")


    number_of_tests = len(test_results)
    for res in test_results:
        if res:
            passed_results += 1

    pass_percentage = float(passed_results * 100 /number_of_tests)
    print("Pass percentage: " + str(pass_percentage) + "%")

    print("========= Test Suite ended ===========")


if __name__=="__main__":
    the = utils.populate_the()
    run_tests(the)
    test_stats()



    
