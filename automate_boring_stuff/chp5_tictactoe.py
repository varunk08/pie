#Tic-tac-toe game in python


theBoard = {
    'topL': '',
    'topM': '',
    'topR': '',
    'midL': '',
    'midM': '',
    'midR': '',
    'botL': '',
    'botM': '',
    'botR': '',
}

def print_board(board):
    print(board['topL'] + ' | ' + board['topM'] + ' | ' + board['topR'])
    print('--+--+--')
    print(board['midL'] + ' | ' + board['midM'] + ' | ' + board['midR'])
    print('--+--+--')
    print(board['botL'] + ' | ' + board['botM'] + ' | ' + board['botR'])


print_board(theBoard)

turn = 'X'
for i in range(9):
    print_board(theBoard)
    print('Turn for ' + turn + ". Move on which space?")
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    print_board(theBoard)

