import re
import liwei.advent as lt

def parse_line(line):
    "parse line return a list of three num"
    return [int(x) for x in re.findall(r'\d+', line)]

def judge(triangle):
    "judge if it is right"
    x, y, z = sorted(triangle)
    return z < x + y

assert judge([3, 1, 8]) == False

print(sum(map(judge, [parse_line(line) for line in lt.Input(3)])))
