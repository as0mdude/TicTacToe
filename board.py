# author: Vincent Fu
# date: May 1, 2023
class Board:
    def __init__(self):
        # board is a list of cells that are represented 
        # by strings (" ", "O", and "X")
        # initially it is made of empty cells represented 
        # by " " strings
        self.sign = " "
        self.size = 3
        self.board = list(self.sign * self.size**2)
        # the winner's sign O or X
        self.winner = ""
    def get_size(self): 
        return self.size
        # optional, return the board size (an instance size)
    def get_winner(self):
        return self.winner
        # return the winner's sign O or X (an instance winner)     
    def set(self, cell, sign):
        num = self.reindex(cell)
        self.board[num] = sign
        # mark the cell on the board with the sign X or O
        # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
        # you can use a tuple ("A1", "B1",...) to obtain indexes 
        # this implementation is up to you 
        
    def reindex(self, cell):
        column = cell[0]
        row = cell[1]
        num = -1
        if column == "a" or column == "A":
            num = 0
        elif column == "b" or column == "B":
            num = 1
        elif column == "c" or column == "C":
            num = 2
        if row == 2 or row=="2":
            num += 3
        elif row == 3 or row=="3":
            num += 6
        return num

    def isempty(self, cell):
        num = self.reindex(cell)
        if num == -1:
            return False
        if self.board[num] == " ":
            return True
        return False
        # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
        # return True if the cell is empty (not marked with X or O)
    def isdone(self):
        self.winner = ''
        lines = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical
            (0, 4, 8), (2, 4, 6),  # diagonal
            ]
    
        for line in lines:
            a, b, c = line
            if self.board[a] == self.board[b] == self.board[c] != " ":
                self.winner = self.board[a]
                return True
    
        if " " not in self.board:
            return True
    
        return False

    def show(self):
     # draw the board
      
        print('   A   B   C') 
        print(' +---+---+---+')
        print('1| {} | {} | {} |'.format(self.board[0], self.board[1], self.board[2]))
        print(' +---+---+---+')
        print('2| {} | {} | {} |'.format(self.board[3], self.board[4], self.board[5]))
        print(' +---+---+---+')
        print('3| {} | {} | {} |'.format(self.board[6], self.board[7], self.board[8]))
        print(' +---+---+---+')