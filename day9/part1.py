f = open("actual.txt", "r")   # open for reading
input_str = f.read()
f.close()

import heapq
import math

from collections import deque
import math
from collections import defaultdict

def rectangle_size(point_x, point_y):
    dx = abs(point_x[0] - point_y[0]) + 1
    dy = abs(point_x[1] - point_y[1]) + 1
    # print(dx)
    # print(dy)
    return dx * dy


print(rectangle_size((2,5), (9,7)))
input_str = input_str.split("\n")
points = []
max_size = float("-inf")
for point in input_str:
    x, y = point.split(",")
    points.append((int(x), int(y)))

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        max_size = max(max_size, rectangle_size(points[i], points[j]))
print(max_size)