import re
import math

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
    n = len(data)
    p = n * percentile / 100
    if p.is_integer():
        return sorted(data)[int(p)]
    else:
        return sorted(data)[int(math.ceil(p)) - 1]

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

the = {}
k, x = re.sub(help, "\n [−][%S]+[%s]+[−][−]([%S]+)[^\n]+= ([%S]+)")
function(k, x)