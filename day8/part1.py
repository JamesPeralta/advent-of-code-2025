f = open("actual.txt", "r")   # open for reading
input_str = f.read()
f.close()

import heapq

from collections import deque
import math
from collections import defaultdict

input_str = input_str.split("\n")


points = []
for line in input_str:
    x, y, z = line.split(",")
    points.append((int(x), int(y), int(z))) 

def distance_between_points(p1, p2):
    p1_x, p1_y, p1_z = p1
    p2_x, p2_y, p2_z = p2

    return math.sqrt((p1_x - p2_x)**2 + (p1_y - p2_y)**2 + (p1_z - p2_z)**2)

dist_points = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = distance_between_points(points[i], points[j])
        heapq.heappush(dist_points, (dist, points[i], points[j]))


neighbs = defaultdict(list)
for i in range(10):
    _, point_a, point_b = heapq.heappop(dist_points)
    neighbs[point_a].append(point_b)
    neighbs[point_b].append(point_a)

def dfs(point, seen, neighbs):
    stack = [point]
    seen.add(point)
    size = 1
    while stack:
        point = stack.pop()
        for neighb in neighbs[point]:
            if neighb in seen:
                continue

            stack.append(neighb)
            seen.add(neighb)
            size += 1

    return size


sizes = []
seen = set()
for point in points:
    if point in seen:
        continue
    
    sizes.append(dfs(point, seen, neighbs))
sizes.sort(reverse=True)
print(sizes)

x, y, z = sizes[:3]
print(x * y * z)
