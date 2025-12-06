f = open("actual.txt", "r")   # open for reading
input_str = f.read()
f.close()

input_str = input_str.split("\n")
# Convert input into 2D matrix

matrix = []
for line in input_str:
    matrix.append([elem for elem in line])

def check_neighbors(matrix, row, col):
    rolls_nearby = 0
    neighbs = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    for d_x, d_y in neighbs:
        curr_row = row + d_x
        curr_col = col + d_y
        if curr_row >= len(matrix) or curr_row < 0:
            continue

        if curr_col >= len(matrix[0]) or curr_col < 0:
            continue
        
        if matrix[curr_row][curr_col] == "@":
            rolls_nearby += 1

    return rolls_nearby

result = 0
changes = True
while changes:
    changes = False
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "@" and check_neighbors(matrix, i, j) < 4:
                result += 1
                matrix[i][j] = "."
                changes = True

print(result)