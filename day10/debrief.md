Part 2

Approach #1
- ​i used rref (reduced row echelon) and then backtracking for nonpivots.
- ​​its rref and then backtracking ontop of it.
- Note: ​​ur backtracking solution space drops massivley by doing rref first
- ​​like for example i only need to consider combinations of the first and second buttons because the third button can be expressed as a lin. comb of the first 2
​​- so u wanna setup a specific matrix Ax = B where x is the # times u press each button and A is the contribution for each button to the total joltage and B is the total wanted Joltage
- ​​which gives u a partial solution because u have free variables in the general case
- ​​and so u do backtracking on the free variables

What to study:
- RREF?
- Linear algebra and linear systems
- constraint satisfaction problems