f = open("actual.txt", "r")   # open for reading
input_str = f.read()
f.close()

input_str = input_str.split("\n")

ranges = []
input_ids = []
for line in input_str:
    if line == "":
        continue
    
    if "-" in line:
        left, right = line.split("-")
        ranges.append([int(left), int(right)])
    else:
        input_ids.append(int(line))

ranges.sort()

result = []
for elem in ranges:
    if len(result) == 0:
        result.append(elem)
        continue
    
    left, right = elem
    if left <= result[-1][1]:
        result[-1] = [result[-1][0], max(result[-1][1], right)]
    else:
        result.append(elem)

output = 0
for left, right in result:
    output += (right - left) + 1
print(output)
