import os
current_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_dir, "inputs/input9.txt")


def main():
    total1 = 0
    total2 = 0

    points = []
    with open(input_path) as f:
        for line in f:
            x,y= map(int, line.strip().split(","))
            points.append((x,y))

    # part 1
    max_area = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]

            width = abs(x1 - x2) + 1
            height = abs(y1 - y2) + 1
            area = width * height
            max_area = max(max_area, area)

    
    total1 = max_area
    # part 2
    # for i in range(len(points))

    print(f"Total1: {total1}")    
    print(f"Total2: {total2}")

if __name__ == "__main__":
    main()

