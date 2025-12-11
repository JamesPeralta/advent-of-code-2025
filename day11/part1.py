
f = open("actual.txt", "r")   # open for reading
input_str = f.read().split("\n")
f.close()

from collections import defaultdict

adj_list = defaultdict(list)
for line in input_str:
    line_split = line.split(": ")
    node = line_split[0]
    neighbs = line_split[1].split()
    for neighb in neighbs:
        adj_list[node].append(neighb)

# print(input_str)

result = 0
stack = ["you"]
while stack:
    cand = stack.pop()
    if cand == "out":
        result += 1
        continue

    for neighb in adj_list[cand]:
        stack.append(neighb)

print(result)