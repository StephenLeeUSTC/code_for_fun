import re
import liwei.advent as lt
from collections import Counter

def parse_line(line):
    "parse line, return (name, sector and checksum"
    return re.match(r'(.+)-(\d+)\[([a-z]+)\]', line).groups()

def parse_sector(line):
    "return parsed sector if valid"
    name, sector, checksum = parse_line(line)
    return int(sector) if valid(name, checksum) else 0

def valid(name, checksum):
    count = Counter(name.replace('-', ''))
    # sort the letter followed the rules
    letters = sorted(count, key = lambda letter : (-count[letter], letter))
    return True if ''.join(letters[:5])== checksum else False

assert parse_sector("aaaaa-bbb-z-y-x-123[abxyz]") == 123
assert valid("aaaaa-bbb-z-y-x", "abxyz")
assert parse_line("aaaaa-bbb-z-y-x-123[abxyz]") == ("aaaaa-bbb-z-y-x", "123", "abxyz")

result = sum(map(parse_sector, lt.Input(4)))
print(result)
