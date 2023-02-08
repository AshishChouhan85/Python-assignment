class Board:

    # FUNCTION TO INITIALIZE NUMBER OF ROWS AND COLUMNS
    def __init__(self):

        self.matrix = []
        self.rows = int(input("Enter number of rows: "))
        self.cols = int(input("Enter number of columns: "))
        

    # FUNCTION TO ENTER CORRECT VALUES IN THE MATRIX
    def make(self):

        for row in range(self.rows):

            temp = []
            
            for col in range(self.cols):

                # RUN AN INFINTE LOOP UNTIL CORRECT VALUE IS ENTERED
                while True:
                    
                    val = input(f"Enter the value for row {row} and col {col}: ")
                    if(val == "O" or val == "X"):
                        temp.append(val)
                        break
                    else:
                        print("Not a valid value")
                        
            self.matrix.append(temp)
            print()
            

    # FUNCTION TO DISPLAY THE MATRIX
    def show(self):

        for row in self.matrix:
            print(row)
        print()

        
    # FUNCTION TO SOLVE THE MATRIX
    def solve(self):
        
        # TRAVERSING THE FIRST COLUMN
        for row in range(self.rows):
    
            self.dfs(row,0)

        # TRAVERSING THE LAST COLUMN
        for row in range(self.rows):
    
            self.dfs(row,self.cols-1)

        # TRAVERSING THE FIRST ROW
        for col in range(self.cols):
    
            self.dfs(0,col)

        # TRAVERSING THE LAST ROW
        for col in range(self.cols):
    
            self.dfs(self.rows-1,col)

        # LOOP TO CHANGE $ -> O AND O -> X
        for row in range(self.rows):
            for col in range(self.cols):
                if(self.matrix[row][col]=="$"):
                    self.matrix[row][col]="O"
                elif(self.matrix[row][col]=="O"):
                    self.matrix[row][col]="X"
                    

    # FUNCTION APPLY DFS ON MATRIX
    def dfs(self, row, col):

        # BASE CASE
        if(row<0 or row==self.rows or col<0 or col==self.cols or self.matrix[row][col]!="O"):
            return

        # AS THE ELEMENT IS O, CHANGE IT TO $
        self.matrix[row][col]="$"

        # MOVE LEFT
        self.dfs(row,col-1)

        # MOVE UP
        self.dfs(row-1,col)

        # MOVE RIGHT
        self.dfs(row,col+1)

        # MOVE DOWN
        self.dfs(row+1,col)
    
        return

# CREATE CLASS OBJECT
board = Board()
print()

# ENTER VALUES IN MATRIX
board.make()

print("Unsolved board")

# SHOWING UNSOLVED BOARD
board.show()

# SOLVING THE BOARD
board.solve()

print("Solved board")

# DISPLAYING SOLVED BOARD
board.show()

