"""
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}

start = [....]
      /
  [..#.]
   /
[.##.]

((0,2) and (0,1))
"""
from collections import deque


f = open("actual.txt", "r")   # open for reading
input_str = f.read().split("\n")
f.close()


def bfs(expected_state, options):
    start = tuple([0 for i in range(len(expected_state))])
    seen = set([start])
    queue = deque([(start, 0)])
    while len(queue):
        candidate, dist = queue.popleft()
        if candidate == expected_state:
            return dist

        for option in options:
            cand_modified = list(candidate)
            for elem in option:
                cand_modified[elem] = 0 if cand_modified[elem] == 1 else 1 
            
            cand_modified = tuple(cand_modified)
            if cand_modified in seen:
                continue
            
            queue.append((cand_modified, dist + 1))
            seen.add(cand_modified)

result = 0
for line in input_str:
    parts = line.split()
    expected_state = tuple([1 if elem == "#" else 0 for elem in parts[0][1:-1]])
    # buttons = [tuple(elem)for elem in parts[1:-1]]
    buttons_str = parts[1:-1]
    buttons = []
    for elem in buttons_str:
        button_ints = elem[1:-1].split(",")
        buttons.append(tuple([int(x) for x in button_ints]))

    joltage = parts[-1]
    result += bfs(expected_state, buttons)
    # print(bfs(expected_state, buttons))
    # print(expected_state, buttons)

print(result)
# input_str = "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"
# expected_state = (0, 1, 1, 0)
# options = [(3,), (1,3), (2,), (2,3), (0,2), (0,1)]

# seen = set([(0,0,0,0)])
# queue = deque([((0,0,0,0), 0)])
# while len(queue):
#     candidate, dist = queue.popleft()
#     if candidate == expected_state:
#         print(dist)
#         break

#     for option in options:
#         cand_modified = list(candidate)
#         for elem in option:
#             cand_modified[elem] = 0 if cand_modified[elem] == 1 else 1 
        
#         cand_modified = tuple(cand_modified)
#         if cand_modified in seen:
#             continue
        
#         queue.append((cand_modified, dist + 1))
#         seen.add(cand_modified)
