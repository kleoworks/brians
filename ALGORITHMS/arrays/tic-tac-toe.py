def tic_tac_toe(arr):

    # variables for counting "x" and "o" spaces on board
    count_x = 0
    count_o = 0


    # player 1 is "x", and plays first
    # player 2 is "o"
    # empty spaces on board are " ", not being tracked in this program
    # count "x" and "o" on board for determing who's turn is next
    for row in range(len(arr)):
        for square in range(len(arr[row])):
            if arr[row][square] == "x":
                count_x +=1
            elif arr[row][square] == "o":
                count_o += 1

    # function to check if any player has won based on current board
    def check_status(player, arr):

        # check if any player has won by getting 3 across or up/down
        for num in range(len(arr)):
            if (arr[num][0] == player and arr[num][1] == player and arr[num][2] == player) or (arr[0][num] == player and arr[1][num] == player and arr[2][num] == player):
                if player == "x":
                    return 'Player 1 won!'
                else:
                    return 'Player 2 won!'

        # check if any player had won by getting diagonal
        if (arr[0][0] == player and arr[1][1] == player and arr[2][2] == player) or (arr[0][2] == player and arr[1][1] == player and arr[2][0] == player):
            if player == "x":
                return 'Player 1 won!'
            else:
                return 'Player 2 won!'


    # call check_status function for both players
    # if any player has won, then end game
    if check_status('x', arr):
        return str(check_status('x', arr)) + ' Game Over'
    elif check_status('o', arr):
        return str(check_status('o', arr)) + ' Game Over'


    # if no one won, who's turn is it?
    # game continues if there are still open squares on board
    if count_x + count_o < 9:

        if count_x > count_o:
            return 'Player 2 turn!'

        else:
            return 'Player 1 turn!'
    else:
        # no open spaces, and no player won
        return 'Cats game! Play Again!'


# tests
board1 = [["x","","x"],["o","x",""],["o","x","o"]] #player 2 turn
board2 = [["x","x","x"],["o","x",""],["o","x","o"]] #player 1 won
board3 = [["x","o","x"],["o","x","o"],["o","x","o"]] #cats game
board4 = [["x","o","x"],["o","x","o"],["o","x","x"]] #player 1 won
board5 = [["x","","x"],["o","o","o"],["","x",""]] #player 2 won
print tic_tac_toe(board1)
print tic_tac_toe(board2)
print tic_tac_toe(board3)
print tic_tac_toe(board4)
print tic_tac_toe(board5)
