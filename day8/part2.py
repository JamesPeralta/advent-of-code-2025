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


class UnionFind:
    def __init__(self):
        self.parent = {}
        self.sizes = defaultdict(int)

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            return x
    
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x == parent_y:
            return False

        size_of_x = self.sizes[parent_x]
        size_of_y = self.sizes[parent_y]
        if size_of_x < size_of_y:
            self.parent[parent_x] = parent_y
        elif size_of_x > size_of_y:
            self.parent[parent_y] = parent_x
        else:
            self.parent[parent_y] = parent_x
            self.sizes[parent_x] += 1

        return True 


neighbs = defaultdict(list)
number_of_components = 9
dsu = UnionFind()
did_connect = []
while dist_points:
    _, point_a, point_b = heapq.heappop(dist_points)
    neighbs[point_a].append(point_b)
    neighbs[point_b].append(point_a)

    new_circuit = dsu.union(point_a, point_b)
    if new_circuit:
        number_of_components -= 1
        did_connect.append((point_a, point_b))

print(did_connect[-1][0][0] * did_connect[-1][1][0])