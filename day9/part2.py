f = open("test.txt", "r")   # open for reading
input_str = f.read()
f.close()

import heapq
import math

from collections import deque
import math
from collections import defaultdict


input_str = input_str.split("\n")
points = []
grid = [["." for j in range(14)] for i in range(9)]

max_size = float("-inf")
min_x, max_x = float("inf"), float("-inf")
min_y, max_y = float("inf"), float("-inf")
for point in input_str:
    x, y = point.split(",")
    x, y = int(x), int(y)
    points.append((x, y))
    # min_x = min(min_x, x)
    # min_y = min(min_y, y)
    # max_x = max(max_x, x)
    # max_y = max(max_y, y)
    grid[y][x] = "#"

for line in grid:
    print("".join(line))

# Fill in the borders

for i in range(1, len(points)):
    point_a, point_b = points[i - 1], points[i]
    same_x = point_a[0] == point_b[0]
    same_y = point_a[1] == point_b[1]
    print(point_a, point_b, "same x" if same_x else "same y")
    if same_x:
        dist = abs(point_a[1] - point_b[1])


        # direction = 1 if point_a[1] - point_b[1] < 0 else -1
        # dist = abs(point_a[1] - point_b[1])
        # curr_y 
        # for i in range(dist):

        # # print(point_a[1] - point_b[1], direction, point_a, point_b)
        # print(direction)
        # curr_
    else:
        dist = abs(point_a[0] - point_b[0])
        curr_x = min(point_a[0], point_b[0])
        curr_y = point_a[1]
        for i in range(dist):
            grid[curr_x][curr_y] = "#"
            curr_x += 1

        # direction = 1 if point_a[0] - point_b[0] < 0 else -1
        # left_most_x = min(point_a[0], point_b[0])
        # print(direction)

# print(points)

# for i in range(len(points)):
#     for j in range(i + 1, len(points)):
#         max_size = max(max_size, rectangle_size(points[i], points[j]))
# print(max_size)