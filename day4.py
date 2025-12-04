from typing import List, Set, Tuple

def day4():
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

    #part 1
    for roll in roll_list:
        adjacent = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                if (roll[0] + dx, roll[1] + dy) in roll_positions:
                    adjacent += 1
                    if adjacent > 3:
                        break
        

        if adjacent < 4:
            total1 += 1

    # part 2:
    processing = True
    while processing:
        processing = False
        for i, roll in enumerate(roll_list):
            adjacent = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    if (roll[0] + dx, roll[1] + dy) in roll_positions:
                        adjacent += 1
                        if adjacent > 3:
                            break
            

            if adjacent < 4:
                processing = True
                del roll_list [i]
                roll_positions.remove(roll)
                total2 += 1
                continue
                


    print(f"Total1: {total1}")    
    print(f"Total2: {total2}")    

if __name__ == "__main__":
    day4()
