def part1(data: list[str]):
    current_positions = {data[0].find("S")}
    total = 0

    for line in data[1:]:
        next_positions = set()
        for position in current_positions:
            if line[position] == "^":
                next_positions.add(position + 1)
                next_positions.add(position - 1)
                total += 1
            else:
                next_positions.add(position)
        current_positions = next_positions
    
    return total

def part2(data):
    starting_position = data[0].find("S")
    memo = {}
    return  find_timelines(starting_position,0, data[1:], memo)

def find_timelines(pos: int,idx: int, data: list[str], memo: dict):
    key = (pos, idx)

    if key in memo:
        return memo[key]
    
    total = 0
    for i in range(idx, len(data)):
        if data[i][pos] == "^":
            total = 0
            total += find_timelines(pos + 1, i + 1, data, memo)
            total += find_timelines(pos - 1, i + 1, data, memo)
            memo[key] = total
            return total
        
    memo[key] = 1
    return 1

def day7():
    with open("input7.txt") as f:
        data = [line.rstrip("\n") for line in f]

    print(f"Total1: {part1(data)}")    
    print(f"Total2: {part2(data)}")    


if __name__ == "__main__":
    day7()


