# author: Vincent Fu
# date: May 1, 2023

from random import choice
from board import Board

class Player:
    def __init__(self, name, sign):
        self.name = name  # player's name
        self.sign = sign  # player's sign O or X
    def get_sign(self):
        return self.sign
        # return an instance sign
    def get_name(self):
        return self.name
        # return an instance name
    def choose(self, board):
        while True:
            print(f"{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ", end="")
            cell = input().strip().lower()
            if len(cell) != 2 or cell[0] not in "abc" or cell[1] not in "123":
                print("You did not choose correctly.")
                continue
            if not board.isempty(cell):
                print("You did not choose correctly.")
                continue
            board.set(cell, self.sign)
            break
    # prompt the user to choose a cell
    # if the user enters a valid string and the cell on the board is empty, update the board
    # otherwise print a message that the input is wrong and rewrite the prompt
    # use the methods board.isempty(cell), and board.set(cell, sign)


class AI(Player):
    def __init__(self, name, sign, board):
        super().__init__(name, sign)
        self.board = board

    def choose(self, board):
        empty_spots = [i for i, spot in enumerate(self.board.board) if spot == " "]
        while True:
            print(f"{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ", end="")
            cell_index = choice(empty_spots)
            row = cell_index // 3
            col = cell_index % 3
            cell_str = ""
            if col == 0:
                cell_str += "a"
            elif col == 1:
                cell_str += "b"
            elif col == 2:
                cell_str += "c"
            cell_str += str(row + 1)
            try:
                self.board.set(cell_str, self.sign)
            except ValueError:
                print("You did not choose correctly.")
            else:
                print(cell_str)
                break

class MiniMax(AI):
    def __init__(self, name, sign, board):
        super().__init__(name, sign, board)
        self.other = "X" if self.sign == "O" else "O" # set the opposite sign of the player

    def choose(self, boardobject):
        # prompt the player for their input
        print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ", end="")
        
        best_score = -99
        cell = -1
        # loop through each cell on the board
        for i in range(len(boardobject.board)):
            if boardobject.board[i] == " ":
                boardobject.board[i] = self.sign
                # calculate the score of each move using the minimax function
                score = self.minimax(boardobject, False, 0)
                boardobject.board[i] = " "
                # choose the cell with the highest score
                if score > best_score:
                    best_score = score
                    cell = i

        # convert the cell index to letter-number coordinates
        if cell % 3 == 0:
            cellstr = "a"
        elif cell % 3 == 1:
            cellstr = "b"
        else:
            cellstr = "c"
        row = (cell // 3) + 1
        cellstr += str(row)

        try:
            # convert the coordinates back to a cell index
            cell = list(cellstr)
            cell[1] = int(cell[1])
            if boardobject.isempty(cell):
                # set the chosen cell to the player's sign
                boardobject.set(cell, self.sign)
                print(cellstr)
            else:
                print("You did not choose correctly.") 
        except:
            print("You did not choose correctly.") 

    def minimax(self, boardobject, self_player, start):
        # check if the game is over and return the score
        if boardobject.isdone():
            if boardobject.get_winner() == self.sign:
                return 1
            elif boardobject.get_winner() == "":
                return 0
            else:
                return -1

        if self_player:
            # maximize the player's score
            best_score = -99
            for i in range(len(boardobject.board)):
                if boardobject.board[i] == " ":
                    boardobject.board[i] = self.sign
                    score = self.minimax(boardobject, False, start + 1)
                    boardobject.board[i] = " "
                    best_score = max(score, best_score)
            return best_score
        else:
            # minimize the opponent's score
            best_score = 99
            for i in range(len(boardobject.board)):
                if boardobject.board[i] == " ":
                    boardobject.board[i] = self.other
                    score = self.minimax(boardobject, True, start + 1)
                    boardobject.board[i] = " "
                    best_score = min(score, best_score)
            return best_score