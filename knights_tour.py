import sys
import time


# Python3 program to solve Knight Tour problem using Backtracking
# Chessboard Size
# run the program by entering "python knights_tour.py <width> <height>" in terminal
# run the program with print at each stage by entering "python knights_tour.py <width> <height> 1" in terminal


# check for bounds of the movable positions
def isSafe(x, y, board, width, height):
    """
        check for bounds and occupancy of the movable positions'

        :param x: the vertical index of the position
        :param y: the horizontal index of the position
        :param board: the 2D board for the problem
        :param width: width of the board
        :param height: the height of the board
        :return: a boolean value. If true that position can be moved to, else the position is not available.
    """

    if 0 <= x < height and 0 <= y < width and board[x][y] == -1:
        return True
    return False


# function to print out the board if there is a solution
def printSolution(width, height, board):
    """
        function to print out the board if there is a solution

        :param width: width of the board
        :param height: the height of the board
        :param board: the 2D board array to be printed
        :return: None. It would print the board.
    """
    for i in range(height):
        for j in range(width):
            print(f"{board[i][j]:>{len(str(width * height)) + 1}}", end=' ')
        print()
    print("*" * width)
    time.sleep(1)


# the outer function for backtracking
def solveKT(width, height, print_stage=False):
    """
        the outer function for backtracking

        :param print_stage: whether print each stage
        :param width: width of the board
        :param height: the height of the board
        :return: print a single solution for the problem
    """
    # Initialization of Board matrix
    board = [[-1 for i in range(width)] for i in range(height)]

    # move_x and move_y define next move of Knight.
    # move_x is for next value of vertical coordinate
    # move_y is for next value of horizontal coordinate
    # This provides all possible next positions for a knight
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # Since the Knight is initially at the first block
    board[0][0] = 0

    # Step counter for knight's position
    pos = 1

    # Checking if solution exists or not
    if not solveKTUtil(width, height, board, 0, 0, move_x, move_y, pos, print_stage):
        print("Solution does not exist")
    else:
        print("Final Result")
        printSolution(width, height, board)


# function uses backtracking to find the answer
def solveKTUtil(width, height, board, curr_x, curr_y, move_x, move_y, pos, print_stage):
    """
        The backtracking function for solving the problem

        :param print_stage: whether print the baord
        :param width: width of the board
        :param height: the height of the board
        :param board: the 2D board array that would be operated upon
        :param curr_x: the vertical index of the position to start from
        :param curr_y: the horizontal index of the position to start from
        :param move_x: the vertical index of the position to move to
        :param move_y: the horizontal index of the position to move to
        :param pos: number of cells visited already
        :return: A boolean value. If true there is a solution, else there is no solution
    """
    if print_stage:
        printSolution(width, height, board)

    if pos == width * height:
        return True

    # Try all next moves from the current coordinate x, y
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if isSafe(new_x, new_y, board, width, height):
            board[new_x][new_y] = pos
            if solveKTUtil(width, height, board, new_x, new_y, move_x, move_y, pos + 1, print_stage):
                return True

            # Backtracking
            board[new_x][new_y] = -1
    return False


# Driver Code
if __name__ == "__main__":
    # Function Call
    if len(sys.argv) != 3 and len(sys.argv) != 4:
        print("python knights_tour.py <width> <height> <(optional)print board: enter 1 to print the board>")
    elif len(sys.argv) == 3:
        print("running")
        solveKT(int(sys.argv[1]), int(sys.argv[2]))
    else:
        if int(sys.argv[3]) != 1:
            print("python knights_tour.py <width> <height> <(optional)print board: enter 1 to print the board>")
        else:
            print("printing")
            solveKT(int(sys.argv[1]), int(sys.argv[2]), True)
