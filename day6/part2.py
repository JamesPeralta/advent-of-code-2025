f = open("actual.txt", "r")   # open for reading
input_str = f.read()
f.close()

input_str = input_str.split("\n")
# Convert input into 2D matrix

def compute_col(matrix, col):
    result = None
    operation = matrix[len(matrix) - 1][col]
    num = []
    for row in range(len(matrix) - 1):
        num.append(matrix[row][col])
    
    as_str = "".join(num).strip()
    if as_str == "":
        return None, None
    return operation.strip(), int("".join(num))

matrix = []
for line in input_str:
    matrix.append([elem for elem in line])

result = 0
curr_nums = []
for col in range(len(matrix[0]) -1, -1, -1):
    operation, num = compute_col(matrix, col)
    if operation == None:
        curr_nums = []
        continue
    
    curr_nums.append(num)
    if operation == "+":
        tmp_result = 0
        for elem in curr_nums:
            tmp_result += elem
        result += tmp_result
    elif operation == "*":
        tmp_result = None
        for elem in curr_nums:
            if tmp_result == None:
                tmp_result = elem
            else:
                tmp_result *= elem
        result += tmp_result

print(result)