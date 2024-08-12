import sys
import time

import matplotlib.pyplot as plt


# Python3 program to solve Knight Tour problem using Backtracking
# Chessboard Size
# run the program by entering "python knights_tour.py <width> <height>" in terminal
# run the program with print at each stage by entering "python knights_tour.py <width> <height> 1" in terminal
# run the program with plotting at each stage by entering "python knights_tour.py <width> <height> 2" in terminal


# move_x and move_y define next move of Knight.
# move_x is for next value of vertical coordinate
# move_y is for next value of horizontal coordinate
# This provides all possible next positions for a knight
# create a tuple store all eight directions
class Board:

    def __init__(self, width, height):
        self.move_x = [2, 2, 1, 1, -2, -2, -1, -1]
        self.move_y = [1, -1, 2, -2, -1, 1, -2, 2]
        self.width = width
        self.height = height

        self.board = [-1 for _ in range(width * height)]
        self.total = width * height

    # check for bounds of the movable positions
    def is_valid(self, x, y):
        # check if the new position is within the board, and whether it is unoccupied.
        return 0 <= x < self.height and 0 <= y < self.width and self.board[x * self.width + y] == -1

    # function to print out the board
    def show_result(self):
        for i in range(self.height):
            for j in range(self.width):
                print(f"{self.board[i * self.width + j]:>{len(str(self.width * self.height)) + 1}}", end=' ')
            print()
        print("*" * self.width)

    # the outer function for backtracking
    def find_tour(self, print_stage=0):
        # The initial position of the knight
        self.board[0] = 0

        # The next position is the index - 1 position.
        count = 1

        if print_stage == 0:
            # Checking if solution exists or not
            start = time.process_time()
            if not self.backtracking(0, 0, count):
                print("Solution not found")
                return
            else:
                print("Final Result")
                self.show_result()
                print(f"Runtime: {time.process_time() - start}")
                return

        elif print_stage == 1:
            if not self.backtracking_print(0, 0, count):
                print("Solution not found")
                return
            else:
                print("Final Result")
                self.show_result()
                return
        else:
            if not self.backtracking_plot(0, 0, count):
                print("Solution not found")
                return
            else:
                print("Final Result")
                self.show_result()
                return

    # function uses backtracking to find the answer
    def backtracking(self, curr_x, curr_y, count):
        # Stop condition of the whole backtrack process.
        # If we traversed all cells in the board, then stop.
        # This function does not return a board, it only manipulates the board.
        if count == self.total:
            return True
        # Try all next moves from the current coordinate x, y
        for i in range(8):
            next_x = curr_x + self.move_x[i]
            next_y = curr_y + self.move_y[i]
            if self.is_valid(next_x, next_y):
                self.board[next_x * self.width + next_y] = count
                if self.backtracking(next_x, next_y, count + 1):
                    return True
                # Backtracking
                self.board[next_x * self.width + next_y] = -1
        # The function would return False if all backtracking process is completed and no solution is found.
        return False

    def backtracking_plot(self, curr_x, curr_y, count):
        # Stop condition of the whole backtrack process.
        # If we traversed all cells in the board, then stop.
        # This function does not return a board, it only manipulates the board.
        if count == self.width * self.height:
            return True

        # Following block is for print purposes.
        # if the parameter is 2, plotting graph using matplotlib
        self.board[curr_x * self.width + curr_y] = self.width * self.height
        self.plot_board()
        self.board[curr_x * self.width + curr_y] = count

        # Try all next moves from the current coordinate x, y
        for i in range(8):
            next_x = curr_x + self.move_x[i]
            next_y = curr_y + self.move_y[i]
            if self.is_valid(next_x, next_y):
                self.board[next_x * self.width + next_y] = count
                if self.backtracking_plot(next_x, next_y, count + 1):
                    return True

                # Backtracking
                self.board[next_x * self.width + next_y] = -1

        # The function would return False if all backtracking process is completed and no solution is found.
        return False

    def backtracking_print(self, curr_x, curr_y, count):
        # Stop condition of the whole backtrack process.
        # If we traversed all cells in the board, then stop.
        # This function does not return a board, it only manipulates the board.
        if count == self.width * self.height:
            return True

        # Following block is for print purposes.
        # if the parameter is 1, print in console logs
        # if the parameter is 2, plotting graph using matplotlib
        self.show_result()
        time.sleep(1)  # set a delay for real-time display

        # Try all next moves from the current coordinate x, y
        for i in range(8):
            next_x = curr_x + self.move_x[i]
            next_y = curr_y + self.move_y[i]
            if self.is_valid(next_x, next_y):
                self.board[next_x * self.width + next_y] = count
                if self.backtracking_print(next_x, next_y, count + 1):
                    return True

                # Backtracking
                self.board[next_x * self.width + next_y] = -1

        # The function would return False if all backtracking process is completed and no solution is found.
        return False

    # Plotting function to provide graph as each stage.
    def plot_board(self):
        board_2d = []
        for i in range(self.height):
            row = self.board[i * self.width:(i + 1) * self.width]
            board_2d.append(row)
        plt.figure(figsize=(10, 10))
        plt.imshow(board_2d, cmap='coolwarm', interpolation='nearest', vmin=-1, vmax=self.width * self.height)
        plt.title('Knight\'s Tour')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.pause(1)  # control the frequency for updated frames
        plt.clf()


# Running the code
if __name__ == "__main__":
    # Function Call
    if len(sys.argv) != 3 and len(sys.argv) != 4:
        print("python knights_tour.py <width> <height> <(optional)print board: enter 1 to print the board or 2"
              " to plot the graph>")
    elif len(sys.argv) == 3:
        print("running")
        b = Board(int(sys.argv[1]), int(sys.argv[2]))
        b.find_tour()
    else:
        if int(sys.argv[3]) != 1 and int(sys.argv[3]) != 2:
            print("python knights_tour.py <width> <height> <(optional)print board: enter 1 to print the board or 2"
                  " to plot the graph>")
        elif int(sys.argv[3]) == 2:
            print("plotting")
            b = Board(int(sys.argv[1]), int(sys.argv[2]))
            b.find_tour(int(sys.argv[3]))
        else:
            print("printing")
            b = Board(int(sys.argv[1]), int(sys.argv[2]))
            b.find_tour(int(sys.argv[3]))
