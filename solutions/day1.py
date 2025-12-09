import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, "../inputs/input1.txt")

def day1():
    current_point = 50
    crosses_count = 0
    zero_count = 0

    with open(input_path) as f:
        for rotation in f:
            distance = int(rotation[1:])

            if rotation.startswith("L"):
                crosses_count -= current_point == 0
                current_point -= distance
                crosses_count -= (current_point // 100) - (1 if current_point % 100 == 0 else 0)
    
            else:
                current_point += distance
                crosses_count += current_point // 100

            current_point = current_point % 100

            if current_point == 0:
                zero_count += 1

    print(f"Final Cross Count: {crosses_count}")
    print(f"Final Zero Count: {zero_count}")


if __name__ == "__main__":
    day1()
