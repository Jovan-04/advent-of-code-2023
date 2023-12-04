from sys import stdin
import re
import math

# red, green, blue cube numbers
CUBE_LAYOUT = [12, 13, 14]

def main():
    total = 0 # part 1
    power_total = 0 # part 2
    for line in stdin.readlines():
        divided = line.split(': ')
        game_num = int(re.findall(r'\d+', divided[0])[0])

        min_colors = calculate_minimum_cubes(divided[1])

        # result for problem 1
        result = [one - two for one, two in zip(CUBE_LAYOUT, min_colors)]

        power_total += math.prod(min_colors)

        if all(x >= 0 for x in result):
            total += game_num

    print(total)
    print(power_total)
    
def calculate_minimum_cubes(game: str) -> list[int]:
    colors = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }

    for pull in re.split('; |, ', game):
        quantity, color = map(str.strip, pull.split(' '))
        if int(quantity) > colors[color]: colors[color] = int(quantity)

    return [colors[x] for x in ['red', 'green', 'blue']]

if __name__ == '__main__':
    main()