# import re
import liwei.advent as lt

Point = complex
N, S, E, W = 1j, -1j, 1, -1 # Unit vectors for headings

def distance(point):
    "City block distance between point and the origin."
    return abs(point.real) + abs(point.imag)

def how_far(moves):
    "After following moves, how far away from the origin do we end up?"
    loc, heading = 0, N # Begin at origin, heading North
    for (turn, dist) in parse(moves):
        heading *= turn
        loc += heading * dist
    return distance(loc)

def parse(text):
    "Return a list of (turn, distance) pairs from text of form 'R2, L42, ...'"
    turns = dict(L=N, R=S)
    return [(turns[RL], int(d)) for (RL, d) in re.findall(r'(R|L)(\d+)', text)]


assert distance(Point(3, 4)) == 7 # City block distance; Euclidean distance would be 5
assert parse('R2, L42') == [(S, 2), (N, 42)]
assert how_far("R2, L3") == 5
assert how_far("R2, R2, R2") == 2
assert how_far("R5, L5, R5, R3") == 12

print(how_far(str(lt.Input(1).read())))

def visited_twice(text):
    "Following moves in text, find the first location we visit twice, and return the distance to it."
    loc, heading = 0, N # Begin at origin, heading North
    visited = {loc}
    for (turn, dist) in parse(text):
        heading *= turn
        for i in range(dist):
            loc += heading
            if loc in visited:
                return distance(loc)
            visited.add(loc)

assert visited_twice("R8, R4, R4, R8") == 4
assert visited_twice("R8, R4, R4, L8") == None
assert visited_twice("R8, R0, R1") == 7

print(visited_twice(lt.Input(1).read()))
