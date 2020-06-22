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

#Minimax algorithm
def miniMax(cur_board,cur_empty,depth,isMax):
    totalScore = 0

    cur_board_copy = copy.copy(cur_board)#Copy board as to not modify the original board
    cur_empty_copy = copy.copy(cur_empty)#Pass on the empty squares on the current board state
    used = copy.copy(cur_empty)#keep track of squares already moved to as to not reuse them.
    
    len_empty = len(cur_empty)
    
    for i in range(len_empty):

        move = random.choice(list(used))
        cur_board_copy[move] = ai_score[isMax][1]
        
        isWin = win(cur_board_copy,ai_score[isMax][1])
        if isWin:  
            return ai_score[isMax][0]
        elif len(used) == 0:
            return 0

        else:
            try:
               used.pop(move)
               cur_empty_copy.pop(move)
            except KeyError:
                return 0
            scr = miniMax(cur_board_copy,cur_empty_copy,depth+1,not isMax)
            cur_board_copy[move] = " "
            cur_empty_copy = copy.copy(cur_empty)

            totalScore += scr

    return totalScore
            

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
        
        scr = miniMax(cur_board,cur_empty,0,False)#True=ai turn, False = Human turn
        
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
ai_score = {True:[1,computer], False:[-1,player], 'tie':0}


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
    
    



    
    




    
