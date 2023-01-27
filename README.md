# Python-assignment

My approach:
Convert all the "O" at boundary to "$". Also, change every "O" connected to "O" at boundary to "$".
The "O" at boundaries can be converted to "$" by traversing along the boundary.
The "O" connected to "O" at boundary can be converted to "$" by doing DFS on "O" at boundary.
Once all the boundaries have been traversed and DFS applied to each "O" at boundary convert the "O" to "X" and "$" to "O".

Steps:
1.) Find row and column of the matrix.
2.) Traverse the first column, if any "O" is found then change it to "$" and apply DFS to it by first moving left, up, right and then down.
3.) Similarly traverse last column, first row and last column.
4.) Once all traversals are completed, do a traversal of the matrix and check each element.
5.) If "$" is found then convert it to "O"
6.) Else if "O" is found then convert it to "X".

