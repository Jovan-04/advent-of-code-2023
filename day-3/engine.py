from sys import stdin
import re
import math

# could be represented by a tuple in fewer lines of code, but i chose to make a class for readability's sake
class Part: 
    def __init__(self, value: int, row: int, start: int, end: int) -> None:
        self.value = value
        self.row = row
        self.start = start
        self.end = end

    def __repr__(self):
        return f'{self.value}: r{self.row} c{self.start}-{self.end}'

def main():
    total = 0 # part 1
    gear_ratio = 0 # part 2
    parts = []
    symbols = []

    # extract all numbers and symbols from the diagram, plus their numbers
    for num, line in enumerate(stdin.readlines()):
        parts.extend(Part(match.group(), num, match.start(), match.start()+len(str(match.group()))) for match in re.finditer(r'\d+', line))
        symbols.extend((num, match.start(), match.group()) for match in re.finditer(r'[-#&%@\+\$\/\*=]', line))

    # part 1 - find all valid parts (adjacent to a symbol)
    # check if each number is a valid part; if so, add it to the total
    for part in parts:
        for sym in symbols:
            if adjacent(part, sym):
                # count the part and then move on to the next part
                total += int(part.value)
                break

    # part 2 - find all gears (* adjacent to exactly two parts)
    for sym in symbols:
        if sym[2] != '*': continue
        adj_parts = []
        for part in parts:
            if adjacent(part, sym):
                adj_parts.append(part.value)
        if len(adj_parts) != 2: continue
        gear_ratio += math.prod(map(int, adj_parts))

    print(total)
    print(gear_ratio)

def adjacent(part: Part, sym):
    # invalid if they're more than one line apart
    if abs(sym[0] - part.row) > 1: return False
    if sym[1] in range(part.start-1, part.end+1): return True
    return False

if __name__ == '__main__':
    main()