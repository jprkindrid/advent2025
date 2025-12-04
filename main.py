
from typing import List, Set, Tuple

def main():
    roll = "@"
    empty = "."
    total1 = 0
    total2 = 0
    total_rolls = 0
    roll_list: List[Tuple[int,int]] = []
    with open("input4.txt") as f:
        for y, line in enumerate(f):
            line = line.strip()

            for x, ch in enumerate(line):
                total_rolls += 1
                if ch == roll:
                    roll_list.append((x, y))

    roll_positions: Set[Tuple[int, int]] = set(roll_list)

    for roll in roll_list:
        adjacent = 0
        possible_positions = [
            (roll[0] + 1, roll[1] + 1),
            (roll[0] + 1, roll[1] - 1),
            (roll[0] - 1, roll[1] + 1),
            (roll[0] - 1, roll[1] - 1),
            (roll[0], roll[1] + 1),
            (roll[0], roll[1] - 1),
            (roll[0] - 1, roll[1]),
            (roll[0] + 1, roll[1]),
        ]
        for pos in possible_positions:
            if pos in roll_positions:
                adjacent += 1
                if adjacent > 3:
                    break

        if adjacent > 3:
            continue

        total1 += 1

    print(f"Total1: {total1}")    
    print(f"Total2: {total2}")    

if __name__ == "__main__":
    main()
