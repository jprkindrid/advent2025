import os
from math import prod


current_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_dir, "inputs/input12.txt")

def get_presents(present_sections: list[str]):
    presents = {}
    for section in present_sections:
        lines = section.split()
        
        key = lines[0].replace(":", "")
        rows = lines[1:]

        presents[key] = rows
    return presents

def lazy_check(regions: list[str], presents: dict[list]):
    valid = 0

    def shape_area(rows):
        return sum(row.count("#") for row in rows)

    present_areas = {k: shape_area(v) for k, v in presents.items()}
    for region in regions:
        parts = region.split()
        w, h = map(int, parts[0].replace(":", "").split("x"))
        region_area = w * h
        counts = parts[1:]

        total_area = 0
        for i, count in enumerate(counts):
            total_area += present_areas[str(i)] * int(count)

        if total_area <= region_area:
            valid += 1
    return valid

def day12():
    total1 = 0

    with open(input_path) as f:
        data = f.read()

    sections = data.split("\n\n")
    presents = get_presents(sections[:-1])
    regions = sections[-1].split("\n")
    print(regions[0])

    total1 += lazy_check(regions, presents)

    # part 1

    print(f"Total1: {total1}")

if __name__ == "__main__":
    day12()