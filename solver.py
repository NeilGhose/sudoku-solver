from sudoku import Board

class Solver:
  def __init__(self, board):
    self.board = board

  def solve(self):
    print(self.board.board)
    for x in range(9):
      for y in range(9):
        if not self.board.board[x][y]:
          for i in range(1,10):
            if(self.board.valid_spot(i,x,y)):
              self.board.set_num(i, x, y)
              self.solve()
          self.board.set_num(0, x, y)
          return
    print(self.board.board)
    input()