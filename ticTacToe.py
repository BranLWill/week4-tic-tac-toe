def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def checkWinner(board, player):    
    print('Checking if ' + player + ' is a winner...')
    
    # Code for checking if either the player O or X has won.
    return ((board['top-L'] == player and board['top-M'] == player and board['top-R'] == player) or # Winner opt across the top
    (board['mid-L'] == player and board['mid-M'] == player and board['mid-R'] == player) or         # Winner opt across the mid
    (board['low-L'] == player and board['low-M'] == player and board['low-R'] == player) or         # Winner opt across the low
    (board['top-L'] == player and board['mid-L'] == player and board['low-L'] == player) or         # Winner opt down the left
    (board['top-M'] == player and board['mid-M'] == player and board['low-M'] == player) or         # Winner opt down the mid
    (board['top-R'] == player and board['mid-R'] == player and board['low-R'] == player) or         # Winner opt down the right
    (board['top-L'] == player and board['mid-M'] == player and board['low-R'] == player) or         # Winner opt for diagonal
    (board['top-R'] == player and board['mid-M'] == player and board['low-L'] == player))           # Winner opt for other diagonal

def startGame(startingPlayer, board):
    turn = startingPlayer# This line is taking startingPlayer and storing ii in the value turn.
    for i in range(9):# This line is the beginning of the for loop from 0-8, therefore running 9 times. 
        printBoard(board)# This line is printing the board after every turn.
        print('Turn for ' + turn + '. Move on which space?')# This line is asking either player O or X to take their turn.
        move = input()# This line is taking the users input and storing it in the value move.
        board[move] = turn# This line is placing the users input on the board.
        if( checkWinner(board, 'X') ):# The lines from 28-30 are checking if the player X has won.
            print('X wins!')
            break
        elif ( checkWinner(board, 'O') ):# The lines from 31-33 are checking if the player O has won.
            print('O wins!')
            break
    
        if turn == 'X':# The line from 35-38 swaps the players from X to O or O to X.
            turn = 'O'
        else:
            turn = 'X'
        
    printBoard(board)# this line prints the TicTac board at the end.
    
