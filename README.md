### CSC 510 SE HW 

Contributors:
- Vinita Ramnani
- Sravanth Reddy Bomanna
- Akash Sarda
- Sidhant Arora
- Arvind Srinivas Subramanian

Classes Implemented:
- Sym : class to calculate mid (mode in symbolic data) and div for symbolic data
- Num : class to calculate mid (median) and standard deviation for numerical data

Functions Implemented:
-  percentile - calculate percentile in a vector of length l
- rnd : generate random real number
- coerce : check for flags in the cli and setting it with values
- o : print a nested hash table
- oo: print a data structure


Tests Implemented:
- test_num : is replica of eg.num test in the given lua code; tests std devidation and median of a numeric vector
- test_sym : tests Sym class; prints mode and diversity of symbol data vector; is a replica of eg.sym
- bignum : replica of eg.bignum; tests if the num class follows the capacity 
-  the : prints the cli options as in the lua source code.

# How to run the tests?

in the src folder, run python3 tests.py

