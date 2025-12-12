"""
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}

start = [....]
      /
  [..#.]
   /
[.##.]

((0,2) and (0,1))

"""
from fractions import Fraction


f = open("actual.txt", "r")   # open for reading
input_str = f.read().split("\n")
f.close()


def rref(matrix):
    """Convert matrix to reduced row echelon form, return (rref_matrix, pivot_cols)"""
    mat = [[Fraction(x) for x in row] for row in matrix]
    rows = len(mat)
    cols = len(mat[0]) if rows > 0 else 0
    
    pivot_cols = []
    pivot_row = 0
    
    for col in range(cols):
        # Find pivot in this column
        max_row = None
        for r in range(pivot_row, rows):
            if mat[r][col] != 0:
                max_row = r
                break
        
        if max_row is None:
            continue  # No pivot in this column, it's a free variable column
        
        # Swap rows
        mat[pivot_row], mat[max_row] = mat[max_row], mat[pivot_row]
        
        # Scale pivot row
        scale = mat[pivot_row][col]
        for c in range(cols):
            mat[pivot_row][c] /= scale
        
        # Eliminate all other rows
        for r in range(rows):
            if r != pivot_row and mat[r][col] != 0:
                factor = mat[r][col]
                for c in range(cols):
                    mat[r][c] -= factor * mat[pivot_row][c]
        
        pivot_cols.append(col)
        pivot_row += 1
        
        if pivot_row >= rows:
            break
    
    return mat, pivot_cols


def solve_with_backtrack(target, buttons):
    """
    Build augmented matrix [A | b], do RREF, identify free variables,
    then backtrack over non-negative integer assignments for free vars.
    """
    ROWS = len(target)
    COLS = len(buttons)
    
    # Build augmented matrix [A | target]
    aug = [[0 for _ in range(COLS + 1)] for _ in range(ROWS)]
    for col, button in enumerate(buttons):
        for row in button:
            aug[row][col] = 1
    for row in range(ROWS):
        aug[row][COLS] = target[row]
    
    # RREF
    rref_mat, pivot_cols = rref(aug)
    
    # Identify free variable columns (not pivot columns, excluding augmented column)
    all_var_cols = set(range(COLS))
    free_cols = sorted(all_var_cols - set(pivot_cols))
    
    # Map pivot columns to their row
    pivot_col_to_row = {col: i for i, col in enumerate(pivot_cols)}
    
    # If no free variables, there's exactly one solution (or none)
    if not free_cols:
        solution = [Fraction(0)] * COLS
        for row_idx, col in enumerate(pivot_cols):
            if col < COLS:
                solution[col] = rref_mat[row_idx][COLS]
        # Check non-negative integers
        if all(x >= 0 and x.denominator == 1 for x in solution):
            return sum(int(x) for x in solution)
        return None
    
    # Backtrack over free variables
    # We need to find bounds for free variables
    # For each free var, we try values starting from 0
    
    best_sum = None
    
    def backtrack(free_idx, free_vals):
        nonlocal best_sum
        
        if free_idx == len(free_cols):
            # All free vars assigned, compute pivot vars
            solution = [Fraction(0)] * COLS
            for i, col in enumerate(free_cols):
                solution[col] = Fraction(free_vals[i])
            
            # Compute pivot variables from RREF
            for row_idx, pcol in enumerate(pivot_cols):
                if pcol >= COLS:
                    continue
                # x_pivot = b - sum(coeff * x_free for free vars)
                val = rref_mat[row_idx][COLS]
                for c in range(COLS):
                    if c != pcol and c not in pivot_cols:
                        val -= rref_mat[row_idx][c] * solution[c]
                solution[pcol] = val
            
            # Check all non-negative integers
            if all(x >= 0 and x.denominator == 1 for x in solution):
                total = sum(int(x) for x in solution)
                if best_sum is None or total < best_sum:
                    best_sum = total
            return
        
        free_col = free_cols[free_idx]
        
        # Estimate upper bound for this free variable
        # Based on constraints, find max value that keeps pivot vars non-negative
        max_val = max(target)  # Simple upper bound
        
        for val in range(max_val + 1):
            # Pruning: if current sum already exceeds best, skip
            current_sum = sum(free_vals) + val
            if best_sum is not None and current_sum >= best_sum:
                break
            backtrack(free_idx + 1, free_vals + [val])
    
    backtrack(0, [])
    return best_sum


def calculate_min(target, buttons):
    result = solve_with_backtrack(target, buttons)
    print(f"Result: {result}")
    return result if result is not None else 0


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