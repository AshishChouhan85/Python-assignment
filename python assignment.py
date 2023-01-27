# FUNCTION TO CHANGE O -> $ IF IT IS AT BORDER OR IT IS CONNECTED TO A O WHICH IS AT BORDER
def solve(i,j):
    global board,row,col

    # BASE CASE
    if(i<0 or i==row or j<0 or j==col or board[i][j]!="O"):
        return

    
    # AS THE ELEMENT IS O, CHANGE IT TO $
    board[i][j]="$"

    # MOVE LEFT
    solve(i,j-1)

    # MOVE UP
    solve(i-1,j)

    # MOVE RIGHT
    solve(i,j+1)

    # MOVE DOWN
    solve(i+1,j)
    
    return
    
    



board = [["O","X","X","O","X"],["X","O","O","X","O"],
         ["X","O","X","O","X"],["O","X","O","O","O"],
         ["X","X","O","X","O"]]

# EXTRACTING ROW AND COLUMN 
row = len(board)
col = len(board[0])


# TRAVERSING THE FIRST COLUMN
for i in range(row):
    
    solve(i,0)

# TRAVERSING THE LAST COLUMN
for i in range(row):
    
    solve(i,col-1)

# TRAVERSING THE FIRST ROW
for j in range(col):
    
    solve(0,j)

# TRAVERSING THE LAST ROW
for j in range(col):
    
    solve(row-1,j)

# LOOP TO CHANGE $ -> O AND O -> X
for i in range(row):
    for j in range(col):
        if(board[i][j]=="$"):
            board[i][j]="O"
        elif(board[i][j]=="O"):
            board[i][j]="X"

print(board)
                                                                                                                                                                       
    

 
