
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

def dfs(node, seen_dac, seen_fft, adj_list, cache):
    if node == "out":
        if seen_dac and seen_fft:
            return 1
        return 0

    if (node, seen_dac, seen_fft) in cache:
        return cache[(node, seen_dac, seen_fft)]

    is_fft = node == "fft"
    is_dac = node == "dac"

    result = 0
    for neighb in adj_list[node]:
        result += dfs(neighb, seen_dac or is_dac, seen_fft or is_fft, adj_list, cache)

    cache[(node, seen_dac, seen_fft)] = result
    return result

print(adj_list)
print(dfs("svr", False, False, adj_list, {}))