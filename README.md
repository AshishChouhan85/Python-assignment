# Python-assignment

## My approach:
1. Convert all the "O" at boundary to "$". Also, change every "O" connected to "O" at boundary to "$".
2. The "O" at boundaries can be converted to "$" by traversing along the boundary.
3. The "O" connected to "O" at boundary can be converted to "$" by doing DFS on "O" at boundary.
4. Once all the boundaries have been traversed and DFS applied to each "O" at boundary convert the "O" to "X" and "$" to "O".

## Steps:
1. Find total rows and total columns of the matrix.
2. Traverse the first column, if any "O" is found then change it to "$" and apply DFS to it by first moving left, up, right and then down.
3. Similarly traverse last column, first row and last column.
4. Once all traversals are completed, do a traversal of the matrix and check each element.
5. If "$" is found then convert it to "O"
6. Else if "O" is found then convert it to "X".
7. Print the board.

## Peer Learning

### Ashwat's approach:
1. He used BFS.
2. First he traversed the boundary of the matrix. If any "O" is found he appended its row and column in the queue.
3. Then he popped the first element from the queue, and changed it to '*'. Then he checked its neighbouring elements (up,down,left and right), if "O" 
   was found then he pushed it in the queue.
4. This process was continued until the queue became empty.
5. Then he traversed the board elements and changed "O" to "X" and "*" to "O".
6. Print the board.

### Srinivas's approach:
#### He has used both DFS and BFS.

#### DFS
1. He traversed the boundary of the matrix and if any "O" is encountered then it is changed to "Y" and DFS is applied to it.
2. If any "O" is encountered in between then it is changed to "Y" and dfs is called for it also. This is performed until no "O" is encountered.
3. Then he traversed the matrix again and changeed "Y" to "O" and "O" to "X".
4. Finally he printed the board.

#### BFS
1. He traversed the boundary of the matrix and if any "O" is encountered then it its row and column are pushed in the queue.
2. Then he pops the first element of the queue and changed it to "Y" and applied BFS to that element. If any "O" was encountered then it was pushed in the queue.
3. This was donw until the queue became empty.
4. Now he traversed the matrix again and changeed "Y" to "O" and "O" to "X".
5. Finally he printed the board.
       




