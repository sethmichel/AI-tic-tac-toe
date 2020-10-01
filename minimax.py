import PlayGame

# scores each tree node will be
# x wins = 10, loses = -10, tie = 0
# so in the tree, each non-winning node will be 0
scores = {"X": 10, "O": -10, "tie": 0}


# Handles AI picking a spot. uses MiniMax
# called by Directory()
# pm board = 2d list of curr game state, mirror of kivy grid
def BestMove(board, openSpots):
    bestScore = -5000   # ai can't possibly get anything smaller than this random small int
    move = ()           # will contain the best move
    score = 0

    # get the scores for all the moves - pick the best one
    for i in range(0, 3):
        for j in range(0, 3):
            if (board[i][j] == ''):                # is the spot available?
                board[i][j] = "O"                  # go there
                score = minimax(board, 0, False, openSpots)   # get the score of that move
                board[i][j] = ''                   # since I move the ai to that spot for tracking purposes, undo that

                if (score > bestScore):            # keep track of best score
                    bestScore = score
                    move = (i, j)

    board[move[0]][move[1]] = "O"                  # do the best move

    print(3 * move[0] + move[1])   # testing
    return 3 * move[0] + move[1]   # need that numb to update gridlayout


# does the actual minimax algorithm to find the score of the next node
# called by BestMove()
# pm board = state of game board
# pm depth = int, depth of tree curr testing
# pm maxPlayer = bool, mini or max, player or computer (X or O)
def minimax(board, depth, maxPlayer, openSpots):
    result = PlayGame.CheckWinner(board, openSpots)
    score = 0
    bestScore = 0

    # terminal node
    if (result != ""):
        return scores[result]

    # else, find the best possible score for all the availble nodes by the AI player
    if (maxPlayer):
        bestScore = -5000

        for i in range(0, 3):
            for j in range(0, 3):               
                if (board[i][j] == ''):                        # Is the spot available?
                    board[i][j] = "O"                           # go there
                    score = minimax(board, depth + 1, False, openSpots)   # recursion, find the max move
                    board[i][j] = ''                           # since I move the X to that spot to tracking purposes, undo that
                    bestScore = max(score, bestScore)

        return bestScore

    # this is the non-ai player
    else:
        bestScore = 5000
        for i in range(0, 3):
            for j in range(0, 3):              
                if (board[i][j] == ''):
                    board[i][j] = "X"                       # move the human here
                    score = minimax(board, depth + 1, True, openSpots)   # recursion, find the mini move
                    board[i][j] = ''
                    bestScore = min(score, bestScore)

        return bestScore

