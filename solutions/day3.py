import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, "../inputs/input3.txt")

def day3():
    total1 = 0
    total2 = 0

    with open(input_path) as f:
        for line in f:
            line = line.strip()

            #part 1
            two_digit_nums = set()
            
            for i in range(len(line)):
                for j in range(i + 1, len(line)):
                    first = int(line[i])
                    second = int(line[j])
                    value = (first * 10) + second
                    two_digit_nums.add(value)
            total1 += max(two_digit_nums)

            #part2
            nums = list(line)
            n = len(nums)
            limit = 12

            to_remove = n - limit
            stack = []

            for d in nums:
                while to_remove > 0 and stack and stack[-1] < d:
                    stack.pop()
                    to_remove -= 1
                stack.append(d)

            stack = stack[:limit]

            total2 += int("".join(stack))


    print(f"Total1: {total1}")    
    print(f"Total2: {total2}")    

if __name__ == "__main__":
    day3()
