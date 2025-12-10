from scipy.optimize import linprog

## [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
##        ------------------------------- ---------
##                variables                 target

c = [1, 1, 1, 1, 1, 1]
tgt = [3, 5, 4, 7]
eqs = [
    [0, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 1, 1, 0],
    [1, 1, 0, 1, 0, 0]
]

bounds = [(0, None)] * 6

res = linprog(c, A_eq=eqs, b_eq=tgt, bounds=bounds, integrality=[1] * 6)
print(int(res.fun), list(map(int, res.x)))