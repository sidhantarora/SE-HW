import re
import math
import os

the = dict()

help='''
    CSV : summarized csv file
    (c) 2022 Tim Menzies <timm@ieee.org> BSD-2 license
    USAGE: lua seen.lua [OPTIONS]
    OPTIONS:
    -e  --eg        start-up example                      = nothing
    -d  --dump      on test failure, exit with stack dump = false
    -f  --file      file with csv data                    = ../data/auto93.csv
    -h  --help      show help                             = false
    -n  --nums      number of nums to keep                = 512
    -s  --seed      random number seed                    = 10019
    -S  --seperator feild seperator                       = ,
'''  

def percentile(data, percentile):
    p = len(data) * percentile / 100
    if p.is_integer():
        ret = sorted(data)[int(p)]
        return ret
    else:
        ret = sorted(data)[int(math.ceil(p)) - 1]
        return ret

def per(t, p):
    import pdb; pdb.set_trace()
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
    try:
        return int(s) or float(s) or fun(re.match(s, "^%s*(.−)%s*$"))
    except RuntimeError as e:
        return None

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
            # import pdb; pdb.set_trace()
            x = re.sub(' +', ' ', token.strip())
            if x == '':
                break
            val = x.split(' = ')[1]
            key = x.split(' = ')[0].split(' ')[1]
            the[key] = val
populate_the()

def o(t):
    print (t)

def oo(t):
    print(o(t))
    return True
    
def csv(name, fun):
    sep = "(^" + the['seperator'] + "^)"
    src = open(name)

    while True:
        s = src.read()
        if not s:
            return src.close()
        else:
            t = dict()
            for s1 in s:
                t[1 + len(t.keys())] = coerce(s1)
            fun(t)

def cli(t):
    for key in t:
        val = str(t[v])
        for k in arg:
            if arg[k] == "-" + key[1] or arg[k] == "--" + key:
                val = (val == "false") and ("true") or (val == "true") and "false" or arg[k + 1]
        t[key] = coerce(v)
    if t['help']:
        print (help)
        os._exit()
    return t
