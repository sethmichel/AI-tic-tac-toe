import os
import sys

# return bool = if there's a 3 in row or either X or O
# called by CheckWinner()
# pm a, b, c = strings, board position contents ('', 'X', or 'O')
def Equals3(a, b, c):
    return (a == b and b == c and a != "")


# returns if there's a winner or not
# called by kivy.btnClicked()
# pm board = 2d list of curr game state, mirror of kivy grid
# pm openSpots = int, # of open spots left on board
def CheckWinner(board, openSpots):
    winner = ""   # will hold X, O, or ""

    # horizontal check
    for i in range(0, 3):
        if (Equals3(board[i][0], board[i][1], board[i][2])):
            winner = board[i][0]

    # vertical check
    for i in range(0, 3):
        if (Equals3(board[0][i], board[1][i], board[2][i])):
            winner = board[0][i]

    # diagonal check
    if (Equals3(board[0][0], board[1][1], board[2][2])):
        winner = board[0][0]

    if (Equals3(board[2][0], board[1][1], board[0][2])):
        winner = board[2][0]

    print(winner)
    # now, be sure the numb of open spots 
    if (winner == "" and openSpots == 0):
        return 'tie'
    else:
        return winner
  
    
