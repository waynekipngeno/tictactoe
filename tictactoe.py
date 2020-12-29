theBoard = {(x + '-' + y):' ' for x in ('top', 'mid', 'low') for y in ('L', 'M', 'R')}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
# printBoard(theBoard)

def checkWin(board):
    winCombs = [['top-L', 'top-M', 'top-R'], ['mid-L', 'mid-M', 'mid-R'], ['low-L', 'low-M', 'low-R'], ['top-L', 'mid-L', 'low-L'], ['top-M', 'mid-M', 'low-M'], ['top-R', 'mid-R', 'low-R'], ['top-L', 'mid-M', 'low-R'], ['top-R', 'mid-M', 'low-L']]
    for comb in winCombs:
        possibleWin = [board[comb[0]].rstrip(), board[comb[1]].rstrip(), board[comb[2]].rstrip()]

        if len(set(possibleWin)) == 1 and list(set(possibleWin))[0] != '':
            
            return comb[0], comb
        
def playTTT():
    import random
    players = ['X', 'O']
    turn = players[random.randint(0,1)]
    for i in range(9):
        win = checkWin(theBoard)
        if win:
            printBoard(theBoard)
            return 'Player {} has won the game! with {}'.format(win[0], win[1])  
         
        else:
            print('It {}\'s turn. Play'.format(turn))
            move = input('Enter move: ')
            theBoard[move] = turn     
            if turn =='X':
                turn = 'O'
            else:
                turn = 'X'
            printBoard(theBoard)  
            
    else:
        print('the game ended in a draw')

playTTT()
