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
    # Goal [3, 5, 4, 7]
    while len(queue):
        candidate, dist = queue.popleft()
        if candidate == expected_state:
            return dist

        for option in options:
            cand_modified = list(candidate)
            for elem in option:
                cand_modified[elem] += 1
            
            should_continue = False
            for i in range(len(cand_modified)):
                if cand_modified[i] > expected_state[i]:
                    should_continue = True
            
            if should_continue:
                continue

            cand_modified = tuple(cand_modified)
            if cand_modified in seen:
                continue
            
            queue.append((cand_modified, dist + 1))
            seen.add(cand_modified)

result = 0
for index, line in enumerate(input_str):
    parts = line.split()
    expected_state = tuple([1 if elem == "#" else 0 for elem in parts[0][1:-1]])
    # buttons = [tuple(elem)for elem in parts[1:-1]]
    buttons_str = parts[1:-1]
    buttons = []
    for elem in buttons_str:
        button_ints = elem[1:-1].split(",")
        buttons.append(tuple([int(x) for x in button_ints]))

    joltage = [int(elem) for elem in parts[-1][1:-1].split(",")]
    # print(joltage, buttons)
    result += bfs(tuple(joltage), buttons)
    print(line1 + " done")

print(result)
"""
(0,3,4,7,9) (0,1,9) (1,2,3,4,5) (0,1,3,7,8) (1,3,4,5,6,7,9)

What is the original matrix?
"""

