class Board:

    # FUNCTION TO INITIALIZE NUMBER OF ROWS AND COLUMNS
    def __init__(self, rows, cols):

        self.matrix = []

        if rows <= 0:
            raise Exception("Invalid rows")

        if cols <= 0:
            raise Exception("Invalid columns")

        self.rows = rows
        self.cols = cols

    # FUNCTION TO VALIDATE NUMBER OF ROWS
    def validate_matrix(self):
        if len(self.matrix) > self.rows:
            raise Exception("Maximum number of rows exceeded")

        if len(self.matrix[0]) > self.cols:
            raise Exception("Maximum number of columns exceeded")

    # FUNCTION TO ENTER CORRECT VALUES IN THE MATRIX
    def check(self):
        for i in self.matrix:
            for j in i:
                if j != 'X' and j != 'O':
                    raise Exception("Invalid input")

    # FUNCTION TO DISPLAY THE MATRIX
    def show(self):

        for row in self.matrix:
            print(row)
        print()

    # FUNCTION TO SOLVE THE MATRIX
    def solve(self):

        # TRAVERSING THE FIRST COLUMN
        for row in range(self.rows):
            self.dfs(row, 0)

        # TRAVERSING THE LAST COLUMN
        for row in range(self.rows):
            self.dfs(row, self.cols - 1)

        # TRAVERSING THE FIRST ROW
        for col in range(self.cols):
            self.dfs(0, col)

        # TRAVERSING THE LAST ROW
        for col in range(self.cols):
            self.dfs(self.rows - 1, col)

        # LOOP TO CHANGE $ -> O AND O -> X
        for row in range(self.rows):
            for col in range(self.cols):
                if self.matrix[row][col] == "$":
                    self.matrix[row][col] = "O"
                elif self.matrix[row][col] == "O":
                    self.matrix[row][col] = "X"

    # FUNCTION APPLY DFS ON MATRIX
    def dfs(self, row, col):

        # BASE CASE
        if row < 0 or row == self.rows or col < 0 or col == self.cols or self.matrix[row][col] != "O":
            return

        # AS THE ELEMENT IS O, CHANGE IT TO $
        self.matrix[row][col] = "$"

        # MOVE LEFT
        self.dfs(row, col - 1)

        # MOVE UP
        self.dfs(row - 1, col)

        # MOVE RIGHT
        self.dfs(row, col + 1)

        # MOVE DOWN
        self.dfs(row + 1, col)

        return


def main():
    # INPUTTING TOTAL NUMBER OF ROWS AND COLUMNS
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    # CREATE CLASS OBJECT
    board = Board(rows, cols)
    print()

    print("Enter X or O as values")

    # ENTER VALUES IN MATRIX
    for i in range(rows):
        board.matrix.append(input().split(" "))

    # VALIDATING NUMBER OF ROWS OR COLUMNS
    board.validate_matrix()

    # VALIDATING INPUT
    board.check()

    print("Unsolved board")

    # SHOWING UNSOLVED BOARD
    board.show()

    # SOLVING THE BOARD
    board.solve()

    print("Solved board")

    # DISPLAYING SOLVED BOARD
    board.show()


if __name__ == "__main__":
    main()
