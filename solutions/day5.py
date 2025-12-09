import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, "../inputs/input5.txt")

def day5():
    total1 = 0
    total2 = 0

    with open(input_path) as f:
        text = f.read().strip()

    range_lines, id_lines = text.split('\n\n')
    range_lines = range_lines.split("\n")
    id_lines = id_lines.split('\n')

    # part1
    ranges = []
    for range_line in range_lines:
        start, end = range_line.split("-")
        ranges.append((int(start), int(end)))

    for id in id_lines:
        for start, end in ranges:
            if start <= int(id) <= end:
                total1 += 1
                break

    # part2
    sorted_ranges = sorted(ranges)
    merged = []
    for start, end in sorted_ranges:
        if merged and start <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))


    total2 = sum(end - start + 1 for start, end in merged)

    print(f"Total1: {total1}")    
    print(f"Total2: {total2}")    

if __name__ == "__main__":
    day5()
