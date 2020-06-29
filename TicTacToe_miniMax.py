import random, copy, time, sys


def choose_ai_dif():
    print('Choose the difficulty of the computer')
    print('1. Easy\n2. Hard')
    while True:
        choice = input()
        if choice == '1':
            return 1
        elif choice == '2':
            return 2
        else:
            print('Please enter either 1 or 2')

def first():
    global player
    global computer
    #'X' always goes first
    print('Choose your marker: X or O')
    while True:
        marker = input()
        if marker.upper() == 'X':
            player = 'X'
            computer = 'O'
            break
        elif marker.upper() == 'O':
            player = 'O'
            computer = 'X'
            break
        else:
            print('Please enter either X or O')

        

def print_board(board):
    print(board['topL'] + '|' + board['topM'] + '|' + board['topR'])
    print('-+-+-')
    print(board['midL'] + '|' + board['midM'] + '|' + board['midR'])
    print('-+-+-')
    print(board['botL'] + '|' + board['botM'] + '|' + board['botR'])
    print('\n')


#WIN?
def win(board, turn):
    return ((board['topL']==turn and board['topM']==turn and board['topR']==turn) or
    (board['midL']==turn and board['midM']==turn and board['midR']==turn) or
    (board['botL']==turn and board['botM']==turn and board['botR']==turn) or
    (board['topL']==turn and board['midL']==turn and board['botL']==turn) or
    (board['topM']==turn and board['midM']==turn and board['botM']==turn) or
    (board['topR']==turn and board['midR']==turn and board['botR']==turn) or
    (board['topL']==turn and board['midM']==turn and board['botR']==turn) or
    (board['topR']==turn and board['midM']==turn and board['botL']==turn))

def get_empty(board):
    #gets all empty squares in the given board state
    empty = []
    for square in board:
        if board[square] == " ":
            empty.append(square)
    
                              
    if len(empty) == 0:
        return 0
    else:
        return empty


def pos_moves(board,turn):
    empty = get_empty(board)
    pos_move =[]
    board_copy = copy.copy(board)
    if empty == 0:
        pos_move.append(board_copy)
        return pos_move
    else:
        for square in empty:
            board_copy[square] = turn
            board_pos = copy.copy(board_copy)
            pos_move.append(board_pos)
            board_copy[square] = " "

    return pos_move
        
#Minimax algorithm
def miniMax(cur_board,depth,isMax):
    maxScore= -2000
    minScore= 2000
    

    turn = ai_score[isMax][1]
    cur_board_copy = copy.copy(cur_board)#Copy board as to not modify the original board
    empty = get_empty(cur_board_copy)
    pos_move = pos_moves(cur_board_copy, turn)
    for i in pos_move:
        #Check if move wins
        isWin = win(i,ai_score[isMax][1])
        if isWin:
            #print('First win')
            return ai_score[isMax][0]
        elif empty == 0:
            return  0
        
        scr = miniMax(i,depth+1,not isMax)
        #print("SCORE")
        #print(scr)
        if isMax and (scr > maxScore):
            maxScore = scr
            
            #print('MAXSCORE')
            #print(maxScore)
        elif isMax == False and (scr < minScore):
            minScore = scr
            #print('MINSCORE')
            #print(minScore)
                
                
            #totalScore += scr
    if isMax:
        return maxScore
    else:
        return minScore

    
            

#RANDOM AI
def ticTacAI():
    print('ticTacAI\'s turn to move!')
    time.sleep(1)
    move = random.choice(list(emptySquare.keys()))
    emptySquare.pop(move)
    print(move)
    board[move] = computer


#Perfect AI
def ticTacAI_Perf():
    print('ticTacAI\'s turn to move!')
    bestScore = -1000
    bestMove = ''

    cur_board = copy.copy(board)
    cur_empty = copy.copy(emptySquare)
    used = copy.copy(emptySquare)
    
    numEmpty = len(emptySquare)
    
    for i in range(numEmpty):
        
        move = random.choice(list(used))
        cur_board[move] = computer
        used.pop(move)
        cur_empty.pop(move)

        #Check for win
        if win(cur_board,computer):
            bestMove = move
            break
        
        scr = miniMax(cur_board,0,False)#True=ai turn, False = Human turn
        cur_empty = copy.copy(emptySquare)
        cur_board[move] = ' '
        
      
        if scr > bestScore:
            bestScore = scr
            bestMove = move
            
    emptySquare.pop(bestMove)
    print(bestMove)
    board[bestMove] = computer
    

#############################################################################

#Global Vars
score=[0,0]
player = 'X'
computer = 'O'
turn = 'X'



print('Welcome to Tic-Tac-Toe Simulator! Try to beat the computer!\n')
print('When it\'s your turn to move, type one of the below options to make a move.')
print('Options are: topL,topM,topR,midL,midM,midR,botL,botM,botR\n')




while True:
    board = {'topL':' ','topM':' ', 'topR':' ',
             'midL':' ','midM':' ', 'midR':' ',
             'botL':' ','botM':' ', 'botR':' '}
    emptySquare = copy.copy(board)

    choice = choose_ai_dif()
    first()
    print_board(board)
    ai_score = {True:[1,computer], False:[-1,player], 'tie':0}

    winner = ''
    
    for i in range(9):
              
        if turn == player:
            while True:
                print('Human\'s turn. Move on which square?')
                move = input()
                if move in emptySquare:
                    break
                else:
                    print('Not a legal move. Options are: topL,topM,topR,midL,midM,midR,botL,botM,botR')
            board[move] = turn
            emptySquare.pop(move)
        elif choice == 1:
            ticTacAI()
            print(1)
        else:
            ticTacAI_Perf()
        
        print_board(board)
        if win(board,turn):
            if turn == player:
                winner = 'Human'
                score[0] += 1
            else:
                winner = 'ticTacAI'
                score[1] += 1
            
            break
        
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    if winner == '':
        winner = 'Nobody'


    print(winner +' wins!')
    print('Human:'+str(score[0])+' ticTacAI:'+str(score[1]))

    
    while True:
        print('play again?(y/n)')
        again = input()
        if again.lower() == 'y':
            turn = 'X'
            break
        elif again.lower() == 'n':
            print('Thanks for playing!')
            time.sleep(1)
            sys.exit()
        else:
            print('please enter \'y\' or \'n\'')
    
    



    
    




    
