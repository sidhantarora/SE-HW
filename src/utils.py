import re
import math
import os
import copy
import sys

the = dict()

help='''
    CSV : summarized csv file
    USAGE: python test.py [OPTIONS]
    OPTIONS:
    -e  --eg        start-up example                      = nothing
    -d  --dump      on test failure, exit with stack dump = false
    -f  --file      file with csv data                    = ../data/auto93.csv
    -h  --help      show help                             = false
    -n  --nums      number of nums to keep                = 512
    -s  --seed      random number seed                    = 10019
    -S  --seperator feild seperator                       = ,
'''  
#options usage yet to be implemented
 
# Usual percentile implmentation - Different from the one in Lua code
def percentile(data, percentile):
    p = len(data) * percentile / 100
    if p.is_integer():
        ret = sorted(data)[int(p)]
        return ret
    else:
        ret = sorted(data)[int(math.ceil(p)) - 1]
        return ret

# Percentile implemntation from the lua code
def per(t, p):
    interim_p = (p / 100) * len(t)
    p = math.floor(interim_p)
    ret = t[max(1, min(len(t), p))]
    return ret

def rnd(x, places):
    mult = 10**(places or 2)
    ret = math.floor(x * mult + 0.5) / mult
    return ret

def coerce(s):
    def fun(s1):
        if s1=="true":
            return True
        if s1=="false":
            return False
        return s1
    if re.match(r'^-?\d+(?:\.\d+)$', s):
        return float(s)
    else:
        return fun(s)

def function(k, x):
    the[k] = coerce(x)
    return the[k]

# return the
def populate_the():
    tokens = help.split('\n')
    flag = False
    for token  in tokens:
        if 'OPTIONS:' in token:
            flag = True
            continue
        if flag:
            x = re.sub(' +', ' ', token.strip())
            if x == '':
                break
            val = x.split(' = ')[1]
            key = x.split(' = ')[0].split(' ')[1]
            the[key] = val
    return the
populate_the()
print(the)
def o(t):
    print (t)

def oo(t):
    print(o(t))
    return True
    

def csv(fname, fun, sep=','):
    # Open the file
    sep = the['--seperator']
    file1 = open(fname, 'r')

    # Read all the lines in the file sepearted by \n
    lines = file1.readlines()
    import pdb; pdb.set_trace()
    # Loop through each line and split each line
    # using the seprator defined previously
    for line in lines:
        t = {}
        line = line[:-1]
        splitLine = line.split(sep)
        for word in splitLine:
            t[1 + len(t.keys())] = coerce(word)
        fun(t)
        print (t)

def iItems(dictVar):
    tempDict = {}
    dictPairs = dictVar.items()
    for dictPair in dictPairs:
        if(isinstance(dictPair[0], int)):
            tempDict[dictPair[0]] = dictPair[1]
        elif(isinstance(dictPair[0], float)):
            break
    return tempDict.items()

def getArgs():
    arguments = sys.argv
    i = 0
    argDict = {}
    for sArgv in arguments:
        argDict[i] = sArgv
        i = i +1

def cli(t):
    args = getArgs()
    for slot,v in t.items():
        v = str(v)
        for n,x in iItems(args):
            if ((x == '-' + slot[1:1]) or (x == '--' + slot)):
                v = (v=='false') and ('true') or (v=='true') and 'false' or args[n+1]
        t[slot] = coerce(v)
    if t['help']:
        print(help)
        os._exit()
    return t

def copy(t):
    if type(t) is not dict:
        return t
    u={}
    for key, value in t.items():
        u[key] = copy(value)
    return u