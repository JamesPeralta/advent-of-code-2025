f = open("actual.txt", "r")   # open for reading
input_str = f.read()
f.close()

input_str = input_str.split("\n")
# Convert input into 2D matrix

def compute_col(matrix, col):
    result = None
    operation = matrix[len(matrix) - 1][col]
    for row in range(len(matrix) - 1):
        if result == None:
            result = int(matrix[row][col])
        elif operation == "+":
            result += int(matrix[row][col])
        else:
            result *= int(matrix[row][col])
    return result

matrix = []
for line in input_str:
    matrix.append([elem for elem in line.split()])

result = 0
for col in range(len(matrix[0])):
    result += compute_col(matrix, col)

print(result)