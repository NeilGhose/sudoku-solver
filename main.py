from sudoku import Board
from solver import Solver

import pygame as pg

def draw_board(board):
  pg.font.init() 
  myfont = pg.font.SysFont('Comic Sans MS', 50)
  s = win.get_size()[1]/3
  for y in range(3):
    for x in range(3):
      pg.draw.rect(win, (0,0,0), (s*x,s*y,win.get_size()[1]/3,win.get_size()[1]/3), 3)
  s /= 3
  for x in range(9):
    pg.draw.line(win, (0,0,0), (s*x, 0), (s*x, s*9))
    pg.draw.line(win, (0,0,0), (0, s*x), (s*9, s*x))
  x = s/5
  for i in board.to_string().split("\n"):
    y = s/5
    for u in i:
      win.blit(myfont.render(u, False, (0, 0, 0)),(y,x))
      y+=s
    x+=s

def draw_selected(board, x, y):
  win.fill(bg_color)
  s = win.get_size()[1]/9
  pg.draw.rect(win, (255,255,0), (s*x,s*y,s,s))
  draw_board(board)

pg.init()

win_size = (800,400)
win=pg.display.set_mode(win_size, pg.RESIZABLE)
pg.display.set_caption("Sudoku")
bg_color = (255,255,255)
win.fill(bg_color)
mouse = pg.mouse
run = True

f = Board()
f.print_board()
solver = Solver(f)
solver.solve()
selected = [0,0]
n=0
while run:
  pg.time.delay(100)
  draw_board(f)
  for i in pg.event.get():
    draw_selected(f, selected[0], selected[1])
    if i.type == pg.QUIT:
      run=False
          
    elif i.type == pg.VIDEORESIZE:
      win_size = i.size
      win=pg.display.set_mode(win_size, pg.RESIZABLE)
      win.fill(bg_color)
    k = pg.key.get_pressed()
        
    if k[pg.K_ESCAPE]:
      run=False

    if k[pg.K_RETURN]:
      print(f.is_invalid())

    if k[pg.K_RIGHT]:
      selected[0] += 1
      if selected[0] == 9:
        selected[0] = 0
        selected[1] += 1
        if selected[1] == 9:
          selected[1] = 0
    if k[pg.K_DOWN]:
      selected[1] += 1
      if selected[1] == 9:
        selected[1] = 8
    if k[pg.K_LEFT]:
      selected[0] -= 1
      if selected[0] == -1:
        selected[0] = 8
        selected[1] -= 1
        if selected[1] == -1:
          selected[1] = 8
    if k[pg.K_UP]:
      selected[1] -= 1
      if selected[1] == -1:
        selected[1] = 0

    if k[pg.K_1]:
      n = 1
    if k[pg.K_2]:
      n = 2
    if k[pg.K_3]:
      n = 3
    if k[pg.K_4]:
      n = 4
    if k[pg.K_5]:
      n = 5
    if k[pg.K_6]:
      n = 6
    if k[pg.K_7]:
      n = 7
    if k[pg.K_8]:
      n = 8
    if k[pg.K_9]:
      n = 9
    if n:
      f.set_num(n, selected[1], selected[0])
      n = 0

  pg.display.update()

pg.quit()

