import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_dir, "inputs/input11.txt")

def dfs1(node, outputs, memo):
    if node == "out":
        return 1
    
    if node in memo:
        return memo[node]
    
    total = 0
    for n in outputs[node]:
        total += dfs1(n, outputs, memo)

    memo[node] = total

    return total

def dfs2(node, outputs, memo, dac, fft):
    new_dac = dac or (node == "dac")
    new_fft = fft or (node == "fft")

    if node == "out":
        return int(new_dac and new_fft)

    key = (node, new_dac, new_fft)

    if key in memo:
        return memo[key]
    
    total = 0
    for n in outputs[node]:
        total += dfs2(n, outputs, memo, new_dac, new_fft)

    memo[key] = total
    return total

def part1(outputs):
    memo = {}
    return dfs1("you", outputs, memo)

def part2(outputs):
    memo = {}
    return dfs2("svr", outputs, memo, False, False)

def day11():
    total1 = 0
    total2 = 0

    with open(input_path) as f:
        lines = [line.strip() for line in f]

    outputs = {}
    for line in lines:
        left, right = line.split(":")
        node = left.strip()
        neighbors = right.split()
        outputs[node] = neighbors

    outputs["out"] == []

    # part 1
    total1 += part1(outputs)
    total2 += part2(outputs)
    

    print(f"Total1: {total1}")
    print(f"Total2: {total2}")

if __name__ == "__main__":
    day11()