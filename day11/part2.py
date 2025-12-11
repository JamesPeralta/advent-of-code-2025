
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

def dfs(node, path, adj_list):
    if node == "out":
        return 1

    result = 0
    for neighb in adj_list[node]:
        dfs(neighb, path, adj_list)

    return result

print(dfs("you", [], adj_list))