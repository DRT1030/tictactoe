import random

board =['1','2','3','4','5','6','7','8','9']; seperator = '|'; n = 0; picker = str(input("Player or bot first?")); sq = 0

def msg1(): print("gg, computer wins")
def msg2(): print("gg, player wins")
at = 0
def botinput():
    global n
    global board
    global at
    at += 1
    win1=[0,4,8]
    win2=[0,3,6]
    win3=[1,4,7]
    win4=[2,5,8]
    win5=[0,1,2]
    win6=[3,4,5]
    win7=[6,7,8]
    win8=[2,4,6]
    n = random.randint(0,8)
    if (board[0] == 'O' and board[4] == 'O') or (board[4] == 'O' and board[8] == 'O') or (board[0] == 'O' and board[8] == 'O'):
        if board[0] == '1': n = 0
        elif board[4] == '5': n = 4
        elif board[8] == '9': n = 8
    elif (board[0] == 'O' and board[3] == 'O') or (board[0] == 'O' and board[6] == 'O') or (board[3] == 'O' and board[6] == 'O'):
        if board[0] == '1': n = 0
        elif board[3] == '4': n = 3
        elif board[6] == '7': n = 6
    
    else:
        while board[n] == 'X' or board[n] == 'O': n = random.randint(0,8)
        
    

    board[n] = 'X'
    for i in range(0, 9, 3): print(board[i] + seperator + board[i+1] + seperator + board[i+2])
    if (board[0] == 'X' and board[4] == 'X' and board [8] == 'X') or (board[0] == 'X' and board[3] == 'X' and board[6] == 'X') or (board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or \
       (board[2] == 'X' and board[5] == 'X' and board[8] == 'X') or (board[0] == 'X' and board[1] == 'X' and board[2] == 'X') or (board[3] == 'X' and board[4] == 'X' and board[5] == 'X') or \
       (board[6] == 'X' and board[7] == 'X' and board[8] == 'X') or (board[2] == 'X' and board[4] == 'X' and board[6] == 'X'): msg1(); board = ['1','2','3','4','5','6','7','8','9']; playerinput()
    else: playerinput()


def playerinput():
    global sq
    global board
    sq = (int(input("Input a number: "))-1)
    if sq == n: print('Bro theres already one, enter a number again'); sq  = int(input()); playerinput()
    else:
        board[sq] = 'O'
    if (board[0] == 'O' and board[4] == 'O' and board[8] == 'O') or (board[0] == 'O' and board[3] == 'O' and board[6] == 'O') or (board[1] == 'O' and board[4] == 'O' and board[7] == 'O') or \
       (board[2] == 'O' and board[5] == 'O' and board[8] == 'O') or (board[0] == 'O' and board[1] == 'O' and board[2] == 'O') or (board[3] == 'O' and board[4] == 'O' and board[5] == 'O') or \
       (board[6] == 'O' and board[7] == 'O' and board[8] == 'O') or (board[2] == 'O' and board[4] == 'O' and board[6] == 'O'): msg2(); board = ['1','2','3','4','5','6','7','8','9']; botinput()
    else: botinput()
    

# TO START THE GAME
if picker == 'Player' or picker.lower() == 'player' or picker == 'p':
    for i in range(0, 9, 3): print(board[i] + seperator + board[i+1] + seperator + board[i+2])
    
else: botinput()
