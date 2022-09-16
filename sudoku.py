import numpy as np
class Board:
  def __init__(self):
    self.board = self.define_board()
    self.editable = np.array([[not i for i in j] for j in self.board])
  
  def define_board(self):
    board = np.array([[3, 0, 6, 5, 0, 8, 4, 0, 0], 
         [5, 2, 0, 0, 0, 0, 0, 0, 0], 
         [0, 8, 7, 0, 0, 0, 0, 3, 1], 
         [0, 0, 3, 0, 1, 0, 0, 8, 0], 
         [9, 0, 0, 8, 6, 3, 0, 0, 5], 
         [0, 5, 0, 0, 9, 0, 6, 0, 0], 
         [1, 3, 0, 0, 0, 0, 2, 5, 0], 
         [0, 0, 0, 0, 0, 0, 0, 7, 4], 
         [0, 0, 5, 2, 0, 6, 3, 0, 0]])
    return board

  def print_board(self):
    print(self.to_string())

  def set_num(self, num, x, y):
    if self.editable[x][y]:
      self.board[x][y] = num

  def line(self, ls):
    x = ls.copy()
    x.sort()
    for i in range(len(x)):
      if i+1 != x[i]:
        return False
    return True

  def valid_spot(self, num, y, x):
    return not (num in self.board[x] or num in [self.board[i][y] for i in range(9)] or num in self.board[(x//3)*3][(y//3)*3:(y//3)*3+3] or num in self.board[(x//3)*3+1][(y//3)*3:(y//3)*3+3] or num in self.board[(x//3)*3+2][(y//3)*3:(y//3)*3+3])
    
  def is_invalid(self):
    for i in self.board:
      if(not self.line(i)):
        return True
    for i in [[j[k] for j in self.board] for k in range(9)]:
      if(not self.line(i)):
        return True
    for x in range(3):
      for y in range(3):
        ls = self.board[x][y:y+3] + self.board[x+1][y:y+3] + self.board[x+2][y:y+3]
        if(not self.line(ls)):
          return True

    return False

  def to_string(self):
    str_ = ""
    for x in self.board:
      for y in x:
        if y:
          str_+=str(y)+""
        else:
          str_+=" "
      str_+="\n"
    return str_

