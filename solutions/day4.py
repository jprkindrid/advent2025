from typing import List, Set, Tuple
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, "../inputs/input4.txt")

def can_remove(roll, roll_positions) -> bool:
    adjacent = 0
    for dx in [-1, 0, 1]:
        if adjacent > 3:
            return False
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            if (roll[0] + dx, roll[1] + dy) in roll_positions:
                adjacent += 1
                if adjacent > 3:
                    return False
                
    return adjacent < 4

def day4():
    roll_char = "@"
    total1 = 0
    total2 = 0
    total_rolls = 0
    roll_list: List[Tuple[int,int]] = []
    with open(input_path) as f:
        for y, line in enumerate(f):
            line = line.strip()

            for x, ch in enumerate(line):
                total_rolls += 1
                if ch == roll_char:
                    roll_list.append((x, y))

    roll_positions: Set[Tuple[int, int]] = set(roll_list)

    #part 1
    for roll in roll_list:
        if can_remove(roll, roll_positions):
            total1 += 1

    # part 2:
    processing = True
    while processing:
        processing = False
        removable = set()
        for roll in roll_list:
            if can_remove(roll, roll_positions):
                removable.add(roll)
                total2 += 1

        if removable:
            processing = True
            roll_list = [roll for roll in roll_list if roll not in removable]
            roll_positions -= removable

    print(f"Total1: {total1}")    
    print(f"Total2: {total2}")    

if __name__ == "__main__":
    day4()
