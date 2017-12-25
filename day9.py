from liwei.advent import Input
import re

pattern = re.compile(r'[(](\d+)x(\d+)[)]')

def decompress(f):
    f = re.sub(r'\s', '', f)
    result = ''
    index = 0
    while index < len(f):
        m = pattern.match(f, index)
        if m:
            n, t = map(int, m.groups())
            index = m.end()
            result += f[index:index + n] * t
            index += n
        else:
            result += f[index]
            index += 1
    return result

print(len(decompress(Input(9).read())))




