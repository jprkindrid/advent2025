from math import prod
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, "../inputs/input6.txt")

def day6():
    total1 = 0
    total2 = 0


    with open(input_path) as f:
        data = [line.rstrip("\n") for line in f]

    with open(input_path) as f:
        tokens = [line.strip().split() for line in f]

    operators = tokens[-1]
    data_lines = tokens[:-1]
    # part1
    for col_idx, operator in enumerate(operators):

        col_values = [int(row[col_idx]) for row in data_lines]
        if operator == "+":
            local_total = sum(col_values)
        elif operator == "*":
            local_total = prod(col_values)
        total1 += local_total
            
    # part2
    height = len(data)
    width = len(data[0])
    grid = [line.ljust(width) for line in data]
    num_rows = height - 1
    buff = [""] * num_rows

    op = None
    buff_idx = 0

    for col in range(width):
        bottom_char = grid[-1][col]

        if bottom_char in ["+", "*"]:
            if op is not None:
                total2 += calc_column(op, buff)
                buff = [""] * num_rows
                
            op = bottom_char
            buff_idx = 0
        
        for row in range(num_rows):
            ch = grid[row][col]
            if ch.isdigit():
                buff[buff_idx] += ch

        buff_idx += 1

    if op is not None:
        total2 += calc_column(op, buff)

    print(f"Total1: {total1}")    
    print(f"Total2: {total2}")    


def calc_column(op, buff):
    nums = [int(s) for s in buff if s != ""]
    if op == "+":
        return sum(nums)
    if op == "*":
        return prod(nums)

if __name__ == "__main__":
    day6()

