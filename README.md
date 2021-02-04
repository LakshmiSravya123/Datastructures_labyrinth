# Datastructures_labyrinth
To receive a maze in the style: 
. . . . . . .
. D . 0 0 0 .
. 0 0 0 . 0 .
. . 0 . . F .
. . 0 0 0 . .
. . 0 . . . .
. . . . . . .
My goal is to solve this labyrinth.

# Specification for input:
1) The labyrinth will always be a square, so if dimension = 10, the labyrinth will be 10 by
10.
2) The labyrinth will come in the format of a long string. So with the labyrinth
previous example: '' ######## D # 000 ## 000 # 0 ### 0 ## F ### 000 ######### ''
3) The '' D '' is the starting point.
4) The '' F '' is the point of arrival.
5) The exterior of the labyrinth is only made up of walls (#).
6) Boxes 0 (zero) are passable, while boxes (#) are non-passable.

# Output Specification
1) A boolean that says if a solution exists or not (true if yes, false if no)
2) A list of tuples (int, int) which gives the exact path to go from box D to
F. Boxes D and F are INCLUDED in the solution (so the first box should be D's
and the last box F's).
3) The boxes go from (0… .d-1, 0… .d-1) in the format (X, Y), the same as a
graph.
The top left box is (0,0) while the bottom right corner will be
(d-1, d-1).
4) The delivery format for the two parameters will be
a tuple.

# Constraints
The solution should be implemented using 1 data structure

# Language 
Python (BFS implementation)
