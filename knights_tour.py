import sys
import time

import matplotlib.pyplot as plt


# Python3 program to solve Knight Tour problem using Backtracking
# Chessboard Size
# run the program by entering "python knights_tour.py <width> <height>" in terminal
# run the program with print at each stage by entering "python knights_tour.py <width> <height> 1" in terminal
# run the program with plotting at each stage by entering "python knights_tour.py <width> <height> 2" in terminal


# check for bounds of the movable positions
def is_valid(x, y, board, width, height):
    """
        check for bounds and occupancy of the movable positions'

        :param x: the vertical index of the position
        :param y: the horizontal index of the position
        :param board: the 2D board for the problem
        :param width: width of the board
        :param height: the height of the board
        :return: a boolean value. If true that position can be moved to, else the position is not available.
    """
    # check if the new position is within the board, and whether it is unoccupied.
    return 0 <= x < height and 0 <= y < width and board[x][y] == -1


# function to print out the board
def show_result(width, height, board):
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


# the outer function for backtracking
def find_tour(width, height, print_stage=0):
    """
        the outer function for backtracking

        :param print_stage: whether print each stage
        :param width: width of the board
        :param height: the height of the board
        :return: print a single solution for the problem
    """
    # Initialization of Board matrix
    board = [[-1 for _ in range(width)] for _ in range(height)]
    empty_board = board

    # move_x and move_y define next move of Knight.
    # move_x is for next value of vertical coordinate
    # move_y is for next value of horizontal coordinate
    # This provides all possible next positions for a knight
    # create a tuple store all eight directions
    move_x = [2, 2, 1, 1, -2, -2, -1, -1]
    move_y = [1, -1, 2, -2, -1, 1, -2, 2]
    move = list(zip(move_x, move_y))

    for i in range(height):
        for j in range(width):
            board = empty_board

            # The initial position of the knight
            board[0][0] = 0

            # The next position is the index - 1 position.
            count = 1

            # Checking if solution exists or not
            if backtracking(width, height, board, 0, 0, move, count, print_stage):
                print("Final Result")
                show_result(width, height, board)
                return

    print("Solution not found")
    return


# function uses backtracking to find the answer
def backtracking(width, height, board, curr_x, curr_y, move, count, print_stage):
    """
        The backtracking function for solving the problem

        :param print_stage: 1 for print to console or 2 to plot graph.
        :param width: width of the board
        :param height: the height of the board
        :param board: the 2D board array that would be operated upon
        :param curr_x: the vertical index of the position to start from
        :param curr_y: the horizontal index of the position to start from
        :param move: the list for all eight possible movements
        :param count: number of cells visited already
        :return: A boolean value. If true there is a solution, else there is no solution
    """

    # Following block is for print purposes.
    # if the parameter is 1, print in console logs
    # if the parameter is 2, plotting graph using matplotlib
    if print_stage == 1:
        show_result(width, height, board)
        time.sleep(1)  # set a delay for real-time display

    elif print_stage == 2:
        board[curr_x][curr_y] = width * height
        plot_board(board, width, height)
        board[curr_x][curr_y] = count

    # Stop condition of the whole backtrack process.
    # If we traversed all cells in the board, then stop.
    # This function does not return a board, it only manipulates the board.
    if count == width * height:
        return True

    # Try all next moves from the current coordinate x, y
    for i in range(8):
        next_x = curr_x + move[i][0]
        next_y = curr_y + move[i][1]
        if is_valid(next_x, next_y, board, width, height):
            board[next_x][next_y] = count
            if backtracking(width, height, board, next_x, next_y, move, count + 1, print_stage):
                return True
            # Backtracking
            board[next_x][next_y] = -1

    # The function would return False if all backtracking process is completed and no solution is found.
    return False


# Plotting function to provide graph as each stage.
def plot_board(board, width, height):
    plt.figure(figsize=(10, 10))
    plt.imshow(board, cmap='coolwarm', interpolation='nearest', vmin=-1, vmax=width * height)
    plt.title('Knight\'s Tour')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.pause(1)  # control the frequency for updated frames
    plt.clf()


# Driver Code
if __name__ == "__main__":
    # Function Call
    if len(sys.argv) != 3 and len(sys.argv) != 4:
        print("python knights_tour.py <width> <height> <(optional)print board: enter 1 to print the board or 2"
              " to plot the graph>")
    elif len(sys.argv) == 3:
        print("running")
        find_tour(int(sys.argv[1]), int(sys.argv[2]))
    else:
        if int(sys.argv[3]) != 1 and int(sys.argv[3]) != 2:
            print("python knights_tour.py <width> <height> <(optional)print board: enter 1 to print the board or 2"
                  " to plot the graph>")
        elif int(sys.argv[3]) == 2:
            print("plotting")
            find_tour(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
        else:
            print("printing")
            find_tour(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
