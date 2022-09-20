### CSC 510 SE HW 

[![Build Status](https://app.travis-ci.com/arvindsrinivas1/SE-HW.svg?branch=main)](https://app.travis-ci.com/github/arvindsrinivas1/SE-HW)
[![Documentation Status](https://readthedocs.org/projects/ansicolortags/badge/?version=latest)](https://github.com/sidhantarora/SE-HW/blob/main/README.md)
<a href =https://github.com/sidhantarora/SE-HW/blob/main/LICENSE.md><img src=https://img.shields.io/github/license/sidhantarora/SE-HW></a>
[![Github Repo size in bytes](https://img.shields.io/github/languages/code-size/sidhantarora/SE-HW)](https://github.com/sidhantarora/SE-HW)
[![codecov](https://codecov.io/gh/arvindsrinivas1/SE-HW/branch/main/graph/badge.svg?token=J984S6M1HO)](https://codecov.io/gh/arvindsrinivas1/SE-HW)

Contributors:
- Vinita Ramnani (vjramnan)
- Sravanth Reddy Bommana (sbomman)
- Akash Sarda (aksarda)
- Sidhant Arora (sarora22)
- Arvind Srinivas Subramanian (asubram9)

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

# Setting up git hooks
We have moved the directory for git hooks to a separate directory called .githooks
To enable this to be the new hooks directory, run the following command:

git config --local core.hooksPath .githooks/


# How to run the tests?
in the root folder, run python3 -m test.test_csv

