import random, time, os

board =['1','2','3','4','5','6','7','8','9']; seperator = '|'; n = 0; picker = str(input("Player or bot first?")); sq = 0
nstorage =[]

def msg1(): print("gg, computer wins")
def msg2(): print("gg, player wins")
turn = 0
nstorage = []
def reset(): nstorage = []
def botinput():
    global n, board, turn, nstorage
    turn += 1
        
    n = random.randint(0,8)
    while board[n] in ['X','O']: n = random.randint(0,8)
    if board[4] == '5': n = 4
    elif (board[0] == 'O' and board[4] == 'O') or (board[4] == 'O' and board[8] == 'O') or (board[0] == 'O' and board[8] == 'O'): n = 0 if board[0] == '1' else 4 if board[4] == '5' else 8 if board[8] == '9' else n
    elif (board[0] == 'O' and board[3] == 'O') or (board[0] == 'O' and board[6] == 'O') or (board[3] == 'O' and board[6] == 'O'): n = 0 if board[0] == '1' else 3 if board[3] == '4' else 6 if board[6] == '7' else n
    elif (board[1] == 'O' and board[4] == 'O') or (board[1] == 'O' and board[7] == 'O') or (board[4] == 'O' and board[7] == 'O'): n = 1 if board[1] == '2' else 4 if board[4] == '5' else 7 if board[7] == '8' else n
    elif (board[2] == 'O' and board[4] == 'O') or (board[2] == 'O' and board[6] == 'O') or (board[4] == 'O' and board[6] == 'O'): n = 2 if board[2] == '3' else 4 if board[4] ==' 5' else 6 if board[6] == '7' else n
    elif (board[2] == 'O' and board[5] == 'O') or (board[2] == 'O' and board[8] == 'O') or (board[5] == 'O' and board[8] == 'O'):
        if board[2] == '3': n = 2
        elif board[5] == '6': n = 5
        elif board[8] == '9': n = 8
    elif (board[0] == 'O' and board[1] == 'O') or (board[0] == 'O' and board[2] == 'O') or (board[1] == 'O' and board[2] == 'O'):
        if board[0] == '1': n = 0
        elif board[1] == '2': n = 1
        elif board[2] == '3': n = 2
    elif (board[3] == 'O' and board[4] == 'O') or (board[3] == 'O' and board[5] == 'O') or (board[4] == 'O' and board[5] == 'O'):
        if board[3] == '4': n = 3
        elif board[4] == '5': n = 4
        elif board[5] == '6': n = 5
    elif (board[6] == 'O' and board[7] == 'O') or (board[6] == 'O' and board[8] == 'O') or (board[7] == 'O' and board[8] == 'O'):
        if board[6] == '7': n = 6
        elif board[7] == '8': n = 7
        elif board[8] == '9': n = 8
    else:   
        while board[n] in ['X','O']: n = random.randint(0,8)

    if (board[0] == 'X' and board[4] == 'X') or (board[4] == 'X' and board[8] == 'X') or (board[0] == 'X' and board[8] == 'X'):
        if board[0] == '1': n = 0
        elif board[4] == '5': n = 4
        elif board[8] == '9': n = 8
    elif (board[0] == 'X' and board[3] == 'X') or (board[0] == 'X' and board[6] == 'X') or (board[3] == 'X' and board[6] == 'X'):
        if board[0] == '1': n = 0
        elif board[3] == '4': n = 3
        elif board[6] == '7': n = 6
    elif (board[1] == 'X' and board[4] == 'X') or (board[1] == 'X' and board[7] == 'X') or (board[4] == 'X' and board[7] == 'X'):
        if board[1] == '2': n = 1
        elif board[4] == '5': n = 4
        elif board[7] == '8': n = 7
    elif (board[2] == 'X' and board[5] == 'X') or (board[2] == 'X' and board[8] == 'X') or (board[5] == 'X' and board[8] == 'X'):
        if board[2] == '3': n = 2
        elif board[5] == '6': n = 5
        elif board[8] == '9': n = 8
    elif (board[0] == 'X' and board[1] == 'X') or (board[0] == 'X' and board[2] == 'X') or (board[1] == 'X' and board[2] == 'X'):
        if board[0] == '1': n = 0
        elif board[1] == '2': n = 1
        elif board[2] == '3': n = 2
    elif (board[3] == 'X' and board[4] == 'X') or (board[3] == 'X' and board[5] == 'X') or (board[4] == 'X' and board[5] == 'X'):
        if board[3] == '4': n = 3
        elif board[4] == '5': n = 4
        elif board[5] == '6': n = 5
    elif (board[6] == 'X' and board[7] == 'X') or (board[6] == 'X' and board[8] == 'X') or (board[7] == 'X' and board[8] == 'X'):
        if board[6] == '7': n = 6
        elif board[7] == '8': n = 7
        elif board[8] == '9': n = 8
    elif (board[2] == 'X' and board[4] == 'X') or (board[2] == 'X' and board[6] == 'X') or (board[4] == 'X' and board[6] == 'X'):
        if board[2] == '3': n = 2
        elif board[4] == '5': n = 4
        elif board[6] == '7': n = 6
    else:   
        while board[n] in ['X','O']: n = random.randint(0,8)
    
    board[n] = 'X'
    
    nstorage.append(n+1)
    
    
    if len(nstorage) >= 5:
        oldestmove = nstorage.pop(0)
        if oldestmove > 0:
            board[oldestmove] = str(int(oldestmove)-1)
    
     
    print("Computers turn")
    
    for i in range(0, 9, 3): print(board[i] + seperator + board[i+1] + seperator + board[i+2])
    if (board[0] == 'X' and board[4] == 'X' and board [8] == 'X') or (board[0] == 'X' and board[3] == 'X' and board[6] == 'X') or (board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or \
       (board[2] == 'X' and board[5] == 'X' and board[8] == 'X') or (board[0] == 'X' and board[1] == 'X' and board[2] == 'X') or (board[3] == 'X' and board[4] == 'X' and board[5] == 'X') or \
       (board[6] == 'X' and board[7] == 'X' and board[8] == 'X') or (board[2] == 'X' and board[4] == 'X' and board[6] == 'X'): msg1(); board = ['1','2','3','4','5','6','7','8','9']; reset(); playerinput()
    elif '1' not in board and '2' not in board and '3' not in board and '4' not in board and '5' not in board and '6' not in board and '7' not in board and '8' not in board and '9' not in board:
        print("DRAW!"); board =['1','2','3','4','5','6','7','8','9'];
        for i in range(0, 9, 3): print(board[i] + seperator + board[i+1] + seperator + board[i+2]);
        playerinput()
    else: playerinput()

def playerinput():
    global sq
    global board
    global turn
    global nstorage
    turn += 1
    
    try:
        sq = (int(input("Input a number: "))-1)
    except (ValueError, IndexError, NameError):
        print('Bro type a number please!'); playerinput()
    if sq > 9:
        print('Bro type a number please!'); playerinput()
    else:
        if sq == n: print('Bro theres already one, enter a number again'); sq  = int(input()) - 1; playerinput()
        else:
            if board[sq] != 'X':
                board[sq] = 'O'
            else:
                print('Bro theres already one, enter a number again'); sq  = int(input()) - 1; playerinput()
    
    nstorage.append(sq+1)
    
    if len(nstorage) >= 5:
        oldestmove = nstorage.pop(0)
        board[oldestmove] = str(oldestmove-1)

    print("Player's turn")
    for i in range(0, 9, 3): print(board[i] + seperator + board[i+1] + seperator + board[i+2])
    if (board[0] == 'O' and board[4] == 'O' and board[8] == 'O') or (board[0] == 'O' and board[3] == 'O' and board[6] == 'O') or (board[1] == 'O' and board[4] == 'O' and board[7] == 'O') or \
           (board[2] == 'O' and board[5] == 'O' and board[8] == 'O') or (board[0] == 'O' and board[1] == 'O' and board[2] == 'O') or (board[3] == 'O' and board[4] == 'O' and board[5] == 'O') or \
           (board[6] == 'O' and board[7] == 'O' and board[8] == 'O') or (board[2] == 'O' and board[4] == 'O' and board[6] == 'O'): msg2(); board = ['1','2','3','4','5','6','7','8','9']; reset(); botinput()
    elif '1' not in board and '2' not in board and '3' not in board and '4' not in board and '5' not in board and '6' not in board and '7' not in board and '8' not in board and '9' not in board:
        print("DRAW!"); board =['1','2','3','4','5','6','7','8','9'];
        for i in range(0, 9, 3): print(board[i] + seperator + board[i+1] + seperator + board[i+2]);
        botinput()
    else: botinput()

# TO START THE GAME
if picker == 'Player' or picker.lower() == 'player' or picker == 'p':
    for i in range(0, 9, 3): print(board[i] + seperator + board[i+1] + seperator + board[i+2])
    playerinput()
else: botinput()
