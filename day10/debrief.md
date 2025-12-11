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

turu sln
- 

11:01 PM
@turuthok
​​Today’s yeah, but for part 2 I used scipy


11:02 PM
@turuthok
​​I feel dirty


11:02 PM
@paul6221
​

#3
​part 2 today reminded me of codeforces


11:02 PM
​​So for example
​​Say for certain target index 0 that needs to be 10, … see which button presses affect 0
​​Suppose that it’s affected by buttons a, b, and e
​​You just need to specify the equation a + b + c = 10
​​Something like that, do it for each target index 0,1,2….
​​And then just run the damn library


  A   B     C   D     E     F     G
 (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}


Yeah, from your example there ... because tgt 0 is affected only by buttons E and F, ... you'd have your first equation as:
[0,0,0,0,1,1] => 3
​​[0,1,0,0,0,1] => 5
[0,0,1,1,1,0] => 4
[1,1,0,1,0,0] => 7

​​from scipy.optimize import linprog
​​res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, integrality=[1,1,1,...])

-> 