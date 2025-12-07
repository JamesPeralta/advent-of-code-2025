f = open("test.txt", "r")   # open for reading
input_str = f.read()
f.close()


from collections import deque
input_str = input_str.split("\n")
# print(input_str)
matrix = []
for line in input_str:
    matrix.append([elem for elem in line])


row_start = 0
col_start = matrix[0].index("S")

"""
.......S.......
.......|.......
......|^.......
......|........
"""

def back_track(matrix, row, col, cache):
    if row >= len(matrix):
        return 0

    if col >= len(matrix[0]) or col < 0:
        return 0

    if row == len(matrix) - 1:
        return 1

    next_row, next_col = row + 1, col
   
    if next_row >= len(matrix):
        return 0

    if next_col >= len(matrix[0]) or next_col < 0:
        return 0

    if (next_row,next_col) in cache:
        return cache[(next_row,next_col)]


    if matrix[next_row][next_col] == ".":
        cache[(next_row,next_col)] = back_track(matrix, next_row, next_col, cache)
        return cache[(next_row,next_col)]
    else:
        cache[(next_row,next_col)] = back_track(matrix, next_row, next_col - 1, cache) + back_track(matrix, next_row, next_col + 1, cache)
        return cache[(next_row,next_col)]

cache = {}
print(back_track(matrix, row_start, col_start, cache))
# queue = deque([(row_start, col_start)])

# seen = set([(row_start, col_start)])
# splits = 0
# while len(queue):
#     row, col = queue.popleft()
#     next_row, next_col = row + 1, col

    
#     if next_row >= len(matrix):
#         continue

#     if next_col >= len(matrix[0]) or next_col < 0:
#         continue

#     if (next_row, next_col) in seen:
#         continue
    
#     matrix[row][col] = "|"
#     if matrix[next_row][next_col] == ".":
#         queue.append((next_row, next_col))
#         seen.add((next_row, next_col))
#     else:
#         splits += 1
#         queue.append((next_row, next_col - 1))
#         queue.append((next_row, next_col + 1))
#         seen.add((next_row, next_col - 1))
#         seen.add((next_row, next_col + 1))
# for line in matrix:
#     print(line)
# # print(matrix)
# print(splits)