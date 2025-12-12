"""
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}

start = [....]
      /
  [..#.]
   /
[.##.]

((0,2) and (0,1))


from scipy.optimize import linprog

c = [1, 1, 1, 1, 1, 1] Objective function. means we want to minimize.

tgt = [3, 5, 4, 7] 

eqs = [
    [0, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 1, 1, 0],
    [1, 1, 0, 1, 0, 0]
]

Set the bounds
bounds = [(0, None)] * 6

res = linprog(c, A_eq=eqs, b_eq=tgt, bounds=bounds, integrality=[1] * 6)
print(int(res.fun), list(map(int, res.x)))

"""
from collections import deque
from scipy.optimize import linprog

f = open("actual.txt", "r")   # open for reading
input_str = f.read().split("\n")
f.close()


def calculate_min(target, buttons):
    c = [1] * len(buttons)

    ROWS = len(target)
    COLS = len(buttons)
    eqs = [[0 for j in range(COLS)] for i in range(ROWS)]
    for col, button in enumerate(buttons):
        for row in button:
            eqs[row][col] = 1

    bounds = [(0, None)] * len(buttons)

    res = linprog(c, A_eq=eqs, b_eq=target, bounds=bounds, integrality=[1] * len(buttons))
    print(res.x)
    res_int = 0
    for elem in res.x:
        res_int += elem
    return int(res_int)


result = 0
for index, line in enumerate(input_str):
    parts = line.split()
    expected_state = tuple([1 if elem == "#" else 0 for elem in parts[0][1:-1]])
    buttons_str = parts[1:-1]
    buttons = []
    for elem in buttons_str:
        button_ints = elem[1:-1].split(",")
        buttons.append(tuple([int(x) for x in button_ints]))

    joltage = [int(elem) for elem in parts[-1][1:-1].split(",")]
    result += calculate_min(joltage, buttons)

print(result)