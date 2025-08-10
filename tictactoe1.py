import pygame,sys
import numpy as np
pygame.init()
#variables
width=600
height=600
line_width=15
board_r=3
board_c=3
circle_w=15
circle_r=60
cross_w=25
cross_s=55
#backgrownd and lines color

bg=(255, 213, 158)
lines_color=(82, 70, 54)
circle_color=(255, 255, 255)
cross_color=(43, 34, 21)
#setting screen
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('TicTacToe')
screen.fill(bg)
#board
board=np.zeros((board_r,board_c))
print(board)
#setting up lines
def lines():
    pygame.draw.line(screen,lines_color,(0,200),(600,200),line_width)
    pygame.draw.line(screen, lines_color, (0, 400), (600, 400), line_width)
    pygame.draw.line(screen, lines_color, (200, 0), (200, 600), line_width)
    pygame.draw.line(screen, lines_color, (400, 0), (400, 600), line_width)

#drawing "0" and "X"
def draw():
    for r in range(board_r):
        for c in range(board_c):
            if board[r][c]==1:
                pygame.draw.circle(screen,circle_color,(int(c*200+100),int(r*200+100)),circle_r,circle_w)
            elif board[r][c]:
                pygame.draw.line(screen,cross_color,(c*200+cross_s,r*200+200-cross_s),(c*200+200-cross_s,r*200+cross_s),cross_w)
                pygame.draw.line(screen,cross_color,(c*200+cross_s,r*200+cross_s),(c*200+200-cross_s,r*200+200-cross_s),cross_w)

def mark(row,col,player):
    board[row][col]=player
def available(row,col):
    if board[row][col]==0:
        return True
    else:
        return False
#setting board to know which block is used     
def board_full():
    for row in range(board_r):
        for col in range(board_c):
         if board[row][col]==0:
             return False
    return True
#checking wining
def checking_win(player):
#vertical check
    for c in range(board_c):
        if board[0][c]==player and board[1][c]==player and board[2][c]==player:
            v_line(c,player)
            return True
#horizontal check
    for r in range(board_r):
        if board[r][0]==player and board[r][1]==player and board[r][2]==player:
            h_line(r,player)
            return True
#corner check
    if board[2][0]==player and board[1][1]==player and board[0][2]==player:
        c1_line(player)
        return True
    if board[0][0]==player and board[1][1]==player and board[2][2]==player:
        c2_line(player)
        return True
    return False

def v_line(c,player):
    ps1=c*200+100
    if player ==1:
        color=circle_color
    elif player==2:
        color=cross_color
    pygame.draw.line(screen,color,(ps1,15),(ps1,height-15),15)
def h_line(r,player):
    ps2=r*200+100
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color
    pygame.draw.line(screen,color,(15,ps2),(width-15,ps2),15)
def c1_line(player):
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color
    pygame.draw.line(screen,color,(15,height-15),(width-15,15),15)
def c2_line(player):
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color
    pygame.draw.line(screen,color,(15,15),(width-15,height-15),15)
#rest function
def reset():
    global board, player, game_over
    board = np.zeros((board_r, board_c))
    player = 1
    game_over = False
    screen.fill(bg)
    lines()
reset()


lines()
player=1
game_over=False
#gameloop
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN and not game_over:
            mousex=event.pos[0]
            mousey=event.pos[1]
            clicked_r=int(mousey//200)
            clicked_c=int(mousex//200)
            if available(clicked_r,clicked_c):
                if player ==1:
                    mark(clicked_r,clicked_c,1)
                    if checking_win(player):
                        game_over=True

                    player=2
                elif player==2:
                    mark(clicked_r,clicked_c,2)
                    if checking_win(player):
                        game_over=True
                    player=1
                draw()
               #the rest key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                reset()

    pygame.display.update()
