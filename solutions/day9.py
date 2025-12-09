from typing import List, Set, Tuple
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_dir, "../inputs/input9.txt")

def day9():
    total1 = 0
    total2 = 0

    vertices: List[Tuple[int, int]] = []
    with open(input_path) as f:
        for line in f:
            x, y = map(int, line.strip().split(","))
            vertices.append((x, y))

    # part 1
    for i, (x1, y1) in enumerate(vertices):
        for x2, y2 in vertices[i + 1:]:
            width = abs(x1 - x2) + 1
            height = abs(y1 - y2) + 1
            total1 = max(total1, width * height)

    # part 2
    edge_points: Set[Tuple[int, int]] = set()
    for idx, (x1, y1) in enumerate(vertices):
        x2, y2 = vertices[(idx + 1) % len(vertices)]
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                edge_points.add((x, y1))
        else:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                edge_points.add((x1, y))

    # I realized after reading around that checking if the complex object (bounding box) perimiter intersects the simple object (rectangle) is probably much faster
    for i, (x1, y1) in enumerate(vertices):
        for x2, y2 in vertices[i + 1:]:
            width = abs(x1 - x2) + 1
            height = abs(y1 - y2) + 1
            area = width * height

            if area <= total2:
                continue

            min_x, max_x = min(x1, x2), max(x1, x2)
            min_y, max_y = min(y1, y2), max(y1, y2)

            valid = True
            for ex, ey in edge_points:
                if min_x < ex < max_x and min_y < ey < max_y:
                    valid = False
                    break

            if valid:
                total2 = area

    print(f"Total1: {total1}")
    print(f"Total2: {total2}")

if __name__ == "__main__":
    day9()