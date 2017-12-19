"""
at last, i follow Petter's code to build mine, i think that just use re to replace abba
will be easily but cost time to write the regular expression, i will try it tomorrow
"""

import liwei.advent as lt
import re

def getsubstring(s, n):
    "from string s get a substring of length n"
    return [s[i:i + n] for i in range(len(s) + 1 - n)]

def abba(string):
    "judge a string if has a substring as abba"
    return any(a == d and b == c and a != b for (a, b, c, d) in getsubstring(string, 4))

assert abba("abba") == True
assert abba("abbc") == False
assert abba("xyabbas") == True

def parseline(line):
    "parse line and return a list of each element"
    return re.split(r"\[|\]", line)

assert parseline('abcs[hhijkj]jkjkj') == ['abcs', 'hhijkj', 'jkjkj']

def getoutside(line):
    return ','.join(parseline(line)[0::2])

def getinside(line):
    return ','.join(parseline(line)[1::2])

def tls(line):
    return abba(getoutside(line)) and not abba(getinside(line))

print(sum(tls(line) for line in lt.Input(7)))

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def ssl(line):
    "judge if a line is a ssl"
    return any(a + b + a in getoutside(line) and b + a + b in
            getinside(line) for a in alphabet for b in alphabet if a != b)

print(sum(ssl(line) for line in lt.Input(7)))
