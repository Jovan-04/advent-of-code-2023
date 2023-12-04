from sys import stdin
import re

def main():
    total_1 = 0
    total_2 = 0
    for line in stdin.readlines():
        matches_1 = [*map(int, re.findall(r'\d', line))]
        total_1 += 10 * matches_1[0] + matches_1[-1]

        matches_2 = [*map(toInt, re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine|zero))', line))]
        total_2 += 10 * matches_2[0] + matches_2[-1]

    print(total_1)
    print(total_2)

num_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0
}

def toInt(string: str):
    num = 0
    try:
        num = int(string)
    except:
        num = num_map[string]
    return num

if __name__ == '__main__':
    main()

