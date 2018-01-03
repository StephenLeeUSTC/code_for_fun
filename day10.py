"""this puzzle may be the hardest one, so sad"""
from collections import defaultdict
from liwei.advent import Input
import re

def bots(instructions, goal={17, 61}):
    "Follow the data flow instructions, and if a bot agets the goal, print it."
    def give(giver, chip, recip):
        "Pass the chip from giver to recipient."
        has[giver].discard(chip)
        has[recip].add(chip)
        chips = has[recip]
        if chips == goal:
            print(recip, 'has', goal)
        if len(chips) == 2:
            give(recip, min(chips), gives[recip][0])
            give(recip, max(chips), gives[recip][1])

    has   = defaultdict(set)       # who has what
    gives = {giver: (dest1, dest2) # who will give what
             for (giver, dest1, dest2)
             in re.findall(r'(bot \d+) gives low to (\w+ \d+) and high to (\w+ \d+)', instructions)}
    for (chip, recip) in re.findall(r'value (\d+) goes to (\w+ \d+)', instructions):
        give('input bin', int(chip), recip)
    return has

has = bots(Input(10).read())

print(has['output 0'].pop() * has['output 1'].pop() * has['output 2'].pop())

