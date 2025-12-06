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

fresh = 0
for input_id in input_ids:
    for left, right in ranges:
        if input_id >= left and input_id <= right:
            fresh += 1
            break

print(fresh)
