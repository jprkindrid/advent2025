from math import sqrt
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, "../inputs/input8.txt")
num_connections = 1000


def day8():
    total1 = 0
    total2 = 0

    points = []
    with open(input_path) as f:
        for line in f:
            x,y,z = map(int, line.strip().split(","))
            points.append((x,y,z))
                    
    def get_distance(p1, p2):
        return sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))
        # sqrt((x1-x2)^2+(y1-y2)^2+(z1-z2)^2) euclidian distance formula thanks claude
    
    pairs = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = get_distance(points[i], points[j])
            pairs.append((distance, i, j))
            
    pairs.sort()
    
    parent = list(range(len(points)))
    def find_root(x):
        if parent[x] != x:
            parent[x] = find_root(parent[x])
        return parent[x]
    
    def find_union(x, y):
        px, py = find_root(x), find_root(y)
        if px != py:
            parent[px] = py
            return True
        return False
    
    connected = 0
    last_i, last_j = None, None
    for iteration, (_, i, j) in enumerate(pairs):
        if find_union(i, j):
            connected += 1
            last_i, last_j = i, j

            # part 1 
            if iteration == num_connections - 1:
                circuts = {}
                for k in range(len(points)):
                    root = find_root(k)
                    if root not in circuts:
                        circuts[root] = 0
                    circuts[root] += 1
                sizes_count = sorted(circuts.values(), reverse=True)
                total1 = sizes_count[0] * sizes_count[1] * sizes_count[2]

            # part 2
            if connected == len(points) - 1:
                total2 = points[last_i][0] * points[last_j][0]
                break

    print(f"Total1: {total1}")    
    print(f"Total2: {total2}")

if __name__ == "__main__":
    day8()

