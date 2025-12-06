f = open("test.txt", "r")   # open for reading
input_str = f.read()
f.close()

input_str = input_str.split("\n")
result = 0
for line in input_str:
    max_res = float("-inf")
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            max_res = max(max_res,int(line[i] + line[j]) )

    result += max_res

print(result)
