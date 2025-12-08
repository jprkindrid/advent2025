from math import sqrt
filename = "input8.txt"
num_connections = 10 if "example" in filename else 1000


def main():
    total1 = 0
    total2 = 0


    points = []
    with open(filename) as f:
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
    print(parent)
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
    for _, i, j in pairs[:num_connections]:
        if find_union(i, j):
            connected += 1
            if connected == num_connections:
                break
            
    circuts = {}
    for i in range(len(points)):
        root = find_root(i)
        if root not in circuts:
            circuts[root] = 0
        circuts[root] += 1
        
    sizes_count = sorted(circuts.values(), reverse=True)
    result = (sizes_count[0] * sizes_count[1] * sizes_count[2])
    total1 += result
    
    print(f"Total1: {total1}")    
    print(f"Total2: {total2}")

if __name__ == "__main__":

    main()

