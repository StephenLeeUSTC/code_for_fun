# import re
import liwei.advent as lt

Keypad = str.split

keypad = Keypad("""
.....
.123.
.456.
.789.
.....
""")

assert keypad[2][2] == '5'

off = '.'

def decode(instructions, x=2, y=2):
    """Follow instructions, keeping track of x, y position, and
    yielding the key at the end of each line of instructions."""
    for line in instructions:
        for C in line:
            x, y = move(C, x, y)
        print(keypad[y][x])
        # yield keypad[y][x]

def move(C, x, y):
    if   C == 'L' and keypad[y][x-1] is not off: x -= 1
    elif C == 'R' and keypad[y][x+1] is not off: x += 1
    elif C == 'U' and keypad[y-1][x] is not off: y -= 1
    elif C == 'D' and keypad[y+1][x] is not off: y += 1
    return x, y

assert move('U', 2, 2) == (2, 1)
assert move('U', 2, 1) == (2, 1)
# assert lt.cat(decode("ULL RRDDD LURDL UUUUD".split())) == '1985'

# lt.cat(decode(lt.Input(2)))
decode(lt.Input(2))
