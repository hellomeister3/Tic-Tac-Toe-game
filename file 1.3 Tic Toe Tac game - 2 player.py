# 52873447.
# My name is AI-17864


def multi_player():
    import os
    board = []
    player1Turn = 1
    player2Turn = 1
    p1turnCounter = True
    p2turnCounter = False
    endgame = False
    what_player = False

    for x in range(0, 3):
        board.append(["■"] * 3)
    # creates the board as a list

    def print_board(board):
        for row in board:
            print(' '.join(row))
    # creates a function for printing the board

    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
    # creates a function to clear the screen

    print_board(board)
    # prints the board

    print('welcome to the Tic Tac Toe game')
    counter1 = str(input('player 1 would you like to be X or O?'))
    if counter1 == 'X':
        counter2 = 'O'
    elif counter1 == 'O':
        counter2 = 'X'
    elif counter1 == 'o':
        counter1 = 'O'
        counter2 = 'X'
    elif counter1 == 'x':
        counter1 = 'X'
        counter2 = 'O'
    else:
        print('that is not a valid character. player 1 is X, player 2 is O')
        counter1 = 'X'
        counter2 = 'O'
    # players choose their counters

    print('player 1 is', counter1, ',player 2 is', counter2)
    # players told what their counters are


    def winner_check(what_player):
        if board[0][0] == board[0][1] == board[0][2] == what_player or \
                board[1][0] == board[1][1] == board[1][2] == what_player or \
                board[2][0] == board[2][1] == board[2][2] == what_player or \
                board[0][0] == board[1][1] == board[2][2] == what_player or \
                board[0][2] == board[1][1] == board[2][0] == what_player or \
                board[0][0] == board[1][0] == board[2][0] == what_player or \
                board[0][1] == board[1][1] == board[2][1] == what_player or \
                board[0][2] == board[1][2] == board[2][2] == what_player:
            return True
        return False
    # see if there are three in a row (\ enables multiple lines in code)

    def tie_check():
        if board[0][0] != '■' and\
                board[0][1] != '■' and\
                board[0][2] != '■' and\
                board[1][0] != '■' and\
                board[1][1] != '■' and\
                board[1][2] != '■' and\
                board[2][0] != '■' and\
                board[2][1] != '■' and\
                board[2][2] != '■':
                return True
        return False
    # checks for if it is a tie


    while endgame == False:

        if p1turnCounter == True:
            print(" player 1 turn", player1Turn)
            player1Turn += 1
            row = int(input("Row: ")) - 1
            col = int(input("Column: ")) - 1
            # player chooses the position for their counter

            if board[row][col] == '■':
                board[row][col] = counter1
                print_board(board) #prints the updated board
                what_player = counter1

            elif IndexError:
                print('this square has already been used, as a penalty your turn is forfeit')#checks for an error
            else:
                print('this square has already been used, as a penalty your turn is forfeit')
            # checks to see if the player has tried to overwrite another counter

            winner_check(what_player)
            tie_check()
            # runs functions for winning conditions


            if tie_check():
                print('its a draw!')
                endgame = True


            if winner_check(what_player) == True:
                print('player 1 wins!')
                endgame = True
                p2turnCounter = False
                p1turnCounter = False
            # code for if player 1 has won

            p1turnCounter = False
            p2turnCounter = True
            # changes the turn

            if winner_check(what_player) == True:
                p2turnCounter = False
            elif tie_check() == True:
                p2turnCounter = False

        elif p2turnCounter == True:
            print(" player 2 turn", player2Turn)
            player2Turn += 1
            row = int(input("Row: ")) - 1
            col = int(input("Column: ")) - 1
            # player chooses a position for their counter

            if board[row][col] == '■':
                board[row][col] = counter2
                print_board(board) #prints the updated board
                what_player = counter2
            elif IndexError:
                print('this square has already been used, as a penalty your turn is forfeit')#checks for an error
            else:
                print('this square has already been used, as a penalty your turn is forfeit')
            # checks to see if the player has tried to overwrite another counter

            # check_win()
            winner_check(what_player)
            # draw()
            tie_check()# runs functions for winning conditions

            if tie_check():
                print('its a draw!')
                endgame = True

            if winner_check(what_player) == True:
                print('player 2 wins!')
                endgame = True
                p1turnCounter = False
                p2turnCounter = False
            # code for if player 2 has won

            p2turnCounter = False
            p1turnCounter = True
            # changes the turn

            if winner_check(what_player) == True:
                p1turnCounter = False
            elif tie_check() == True:
                p1turnCounter = False


def single_player():
    board = []
    players_turn = True
    AI_playing = False
    endgame = False
    player1Turn = 1
    AI_turn = 1

    for x in range(0, 3):
        board.append(["■"] * 3)
    # creates the board as a list

    def print_board(board):
        for row in board:
            print(' '.join(row))
    # creates a function for printing the board

    print_board(board)
    # prints the board

    print('welcome to the Tic Tac Toe game')
    counter1 = str(input('player 1 would you like to be X or O?'))
    if counter1 == 'X':
        AI_counter = 'O'
    elif counter1 == 'O':
        AI_counter = 'X'
    elif counter1 == 'o':
        counter1 = 'O'
        AI_counter = 'X'
    elif counter1 == 'x':
        counter1 = 'X'
        AI_counter = 'O'
    else:
        print('that is not a valid character. player 1 is X, player 2 is O')
        counter1 = 'X'
        AI_counter = 'O'
    # players choose their counters

    print('player 1 is', counter1, ',the AI is', AI_counter)
    # players told what their counters are

    def winner_check(what_player):
        if board[0][0] == board[0][1] == board[0][2] == what_player or \
                board[1][0] == board[1][1] == board[1][2] == what_player or \
                board[2][0] == board[2][1] == board[2][2] == what_player or \
                board[0][0] == board[1][1] == board[2][2] == what_player or \
                board[0][2] == board[1][1] == board[2][0] == what_player or \
                board[0][0] == board[1][0] == board[2][0] == what_player or \
                board[0][1] == board[1][1] == board[2][1] == what_player or \
                board[0][2] == board[1][2] == board[2][2] == what_player:
            return True
        return False
    # see if there are three in a row (\ enables multiple lines in code)

    def tie_check():
        if board[0][0] != '■' and \
                board[0][1] != '■' and \
                board[0][2] != '■' and \
                board[1][0] != '■' and \
                board[1][1] != '■' and \
                board[1][2] != '■' and \
                board[2][0] != '■' and \
                board[2][1] != '■' and \
                board[2][2] != '■':
            return True
        return False
    # checks for if it is a tie

    def total_checking():

        winner_check(what_player)
        tie_check()
        # runs functions for winning conditions

    def check_outcomes():
        if tie_check():
            print('its a draw!')
            endgame = True
            players_turn = False
            AI_playing = False

        elif winner_check(what_player) == True:
            print('unlucky, the AI won!')
            endgame = True
            players_turn = False
            AI_playing = False
        # code for if player 1 has won


    # stops the game if it is a tie or a win

    while endgame == False:

        if players_turn == True:
            print(" player 1 turn", player1Turn)
            player1Turn += 1
            row = int(input("Row: ")) - 1
            col = int(input("Column: ")) - 1
            # player chooses the position for their counter

            if board[row][col] == '■':
                board[row][col] = counter1
                print_board(board) #prints the updated board
                what_player = counter1
            elif IndexError:
                print('this square has already been used, as a penalty your turn is forfeit')#checks for an error
            else:
                print('this square has already been used, as a penalty your turn is forfeit')
            # checks to see if the player has tried to overwrite another counter


            winner_check(what_player)
            tie_check()
            # runs functions for winning conditions


            if tie_check():
                print('its a draw!')
                endgame = True
                players_turn = False
                AI_playing = False

            elif winner_check(what_player) is True:
                print('player 1 wins!')
                endgame = True
                players_turn = False
                AI_playing = False
            # code for if player 1 has won

            else:
                pass
                # stops the game if it is a tie or a win

            if endgame == False:
                players_turn = False
                AI_playing = True

        elif AI_playing == True:
            print('AI turn', AI_turn)
            AI_turn += 1

            if (board[0][0] == counter1 or
                    board[0][2] == counter1 or
                    board[2][0] == counter1 or
                    board[2][2] == counter1) and \
                    board[1][1] == '■':
                board[1][1] = AI_counter
                print_board(board)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
            # tells the AI to play in the middle square if its opponent has gone in the corners.

            elif (board[0][1] == counter1 or
                    board[1][2] == counter1 or
                    board[2][1] == counter1 or
                    board[1][0] == counter1) and \
                    board[1][1] == '■':
                board[1][1] = AI_counter
                print_board(board)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
            # tells the AI to play in the middle if its opponent has gone in one of the sides.

            elif board[1][1] == counter1 and \
                    board[0][0] == '■':
                board[0][0] = AI_counter
                print_board(board)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
            # tells the AI to play in the top corner if its opponent has played in the middle.

            elif board[1][1] == counter1 and \
                    board[2][2] == '■' or \
                    board[0][0] == counter1 and \
                    board[2][0] == counter1 and \
                    board[2][1] == counter1 and \
                    board[2][2] == '■':
                board[2][2] = AI_counter
                print_board(board)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
            # counters the opponent if they have 2 in a row

            elif board[2][0] == counter1 and \
                    board[1][1] == counter1 and \
                    board[0][2] == '■' or \
                    board[0][0] == counter1 and \
                    board[0][1] == counter1 and \
                    board[0][2] == '■':
                board[0][2] = AI_counter
                print_board(board)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
            # counters the opponent if they have 2 in a row

            elif board[0][2] == counter1 and \
                    board[0][1] == counter1 and \
                    board[0][0] == '■' or \
                    board[1][0] == counter1 and \
                    board[2][0] == counter1 and \
                    board[0][0] == '■':
                board[0][0] = AI_counter
                print_board(board)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
            # counters the opponent if they have 2 in a row

            elif board[1][0] == counter1 and \
                    board[0][0] == counter1 and \
                    board[2][0] == '■' or \
                    board[2][1] == counter1 and \
                    board[2][2] == counter1 and \
                    board[2][0] == '■':
                board[2][0] = AI_counter
                print_board(board)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
            # counters the opponent if they have 2 in a row

            elif board[2][1] == counter1 and \
                    board[1][1] == counter1 and \
                    board[0][1] == '■' or \
                    board[0][0] == counter1 and \
                    board[0][2] == counter1 and \
                    board[0][1] == '■':
                board[0][1] = AI_counter
                print_board(board)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
            # counters the opponent if they have 2 in a row

            elif board[1][0] == counter1 and \
                    board[1][1] == counter1 and \
                    board[1][2] == '■' or \
                    board[0][2] == counter1 and \
                    board[2][2] == counter1 and \
                    board[1][2] == '■':
                board[1][2] = AI_counter
                print_board(board)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
            # counters the opponent if they have 2 in a row

            elif board[0][1] == counter1 and \
                    board[1][1] == counter1 and \
                    board[2][1] == '■' or \
                    board[2][2] == counter1 and \
                    board[2][0] == counter1 and \
                    board[2][2] == '■':
                board[2][1] = AI_counter
                print_board(board)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
            # counters the opponent if they have 2 in a row

            elif board[1][2] == counter1 and \
                    board[1][1] == counter1 and \
                    board[1][0] == '■' or \
                    board[0][0] == counter1 and \
                    board[2][0] == counter1 and \
                    board[1][0] == '■':
                board[1][0] = AI_counter
                print_board(board)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
            # counters the opponent if they have 2 in a row

            elif board[0][0] == counter1 and \
                    board[2][2] == counter1 and \
                    board[1][1] == '■' or \
                    board[2][0] == counter1 and \
                    board[0][2] == counter1 and \
                    board[1][1] == '■' or \
                    board[0][1] == counter1 and \
                    board[2][1] == counter1 and \
                    board[1][1] == '■' or \
                    board[1][0] == counter1 and \
                    board[1][2] == counter1 and \
                    board[1][1] == '■':
                board[1][1] = AI_counter
                print_board(board)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
            # counters the opponent if they have 2 around the centre.

            elif board[1][1] == AI_counter and \
                     board[0][0] == AI_counter and \
                     board[2][2] == '■' or \
                     board[2][0] == AI_counter and \
                     board[2][1] == AI_counter and \
                     board[2][2] == '■':
                board[2][2] = AI_counter
                print_board(board)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
                # Tells AI to play the third in arrow if the player has not countered it

            elif board[2][0] == AI_counter and \
                     board[1][1] == AI_counter and \
                     board[0][2] == '■' or \
                     board[0][0] == AI_counter and \
                     board[0][1] == AI_counter and \
                     board[0][2] == '■':
                board[0][2] = AI_counter
                print_board(board)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
                # Tells AI to play the third in arrow if the player has not countered it

            elif board[0][2] == AI_counter and \
                     board[0][1] == AI_counter and \
                     board[0][0] == '■' or \
                     board[1][0] == AI_counter and \
                     board[2][0] == AI_counter and \
                     board[0][0] == '■':
                board[0][0] = AI_counter
                print_board(board)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
                # Tells AI to play the third in arrow if the player has not countered it

            elif board[1][0] == AI_counter and \
                     board[0][0] == AI_counter and \
                     board[2][0] == '■' or \
                     board[2][1] == AI_counter and \
                     board[2][2] == AI_counter and \
                     board[2][0] == '■':
                board[2][0] = AI_counter
                print_board(board)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
                # Tells AI to play the third in arrow if the player has not countered it

            elif board[2][1] == AI_counter and \
                     board[1][1] == AI_counter and \
                     board[0][1] == '■' or \
                     board[0][0] == AI_counter and \
                     board[0][2] == AI_counter and \
                     board[0][1] == '■':
                board[0][1] = AI_counter
                print_board(board)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
                # Tells AI to play the third in arrow if the player has not countered it

            elif board[1][0] == AI_counter and \
                     board[1][1] == AI_counter and \
                     board[1][2] == '■' or \
                     board[0][2] == AI_counter and \
                     board[2][2] == AI_counter and \
                     board[1][2] == '■':
                board[1][2] = AI_counter
                print_board(board)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
                # Tells AI to play the third in arrow if the player has not countered it

            elif board[0][1] == AI_counter and \
                     board[1][1] == AI_counter and \
                     board[2][1] == '■' or \
                     board[2][2] == AI_counter and \
                     board[2][0] == AI_counter and \
                     board[2][2] == '■':
                board[2][1] = AI_counter
                print_board(board)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
                # counters the opponent if they have 2 in a row

            elif board[1][2] == AI_counter and \
                     board[1][1] == AI_counter and \
                     board[1][0] == '■' or \
                     board[0][0] == AI_counter and \
                     board[2][0] == AI_counter and \
                     board[1][0] == '■':
                board[1][0] = AI_counter
                print_board(board)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
                # Tells AI to play the third in arrow if the player has not countered it

            elif board[0][0] == AI_counter and \
                     board[2][2] == AI_counter and \
                     board[1][1] == '■' or \
                     board[2][0] == AI_counter and \
                     board[0][2] == AI_counter and \
                     board[1][1] == '■' or \
                     board[0][1] == AI_counter and \
                     board[2][1] == AI_counter and \
                     board[1][1] == '■' or \
                     board[1][0] == AI_counter and \
                     board[1][2] == AI_counter and \
                     board[1][1] == '■':
                board[1][1] = AI_counter
                print_board(board)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
                # Tells AI to play the third in arrow if the player has not countered it

            else:
                if board[0][0] == '■':
                    board[0][0] = AI_counter
                    print_board(board)
                    players_turn = True
                    AI_playing = False

                elif board[0][1] == '■':
                    board[0][1] = AI_counter
                    print_board(board)
                    players_turn = True
                    AI_playing = False

                elif board[0][2] == '■':
                    board[0][2] = AI_counter
                    print_board(board)
                    players_turn = True
                    AI_playing = False

                elif board[1][0] == '■':
                    board[1][0] = AI_counter
                    print_board(board)
                    players_turn = True
                    AI_playing = False

                elif board[1][1] == '■':
                    board[1][1] = AI_counter
                    players_turn = True
                    AI_playing = False

                elif board[1][2] == '■':
                    board[1][2] = AI_counter
                    print_board(board)
                    players_turn = True
                    AI_playing = False

                elif board[2][0] == '■':
                    board[2][0] = AI_counter
                    print_board(board)
                    players_turn = True
                    AI_playing = False

                elif board[2][1] == '■':
                    board[2][1] = AI_counter
                    print_board(board)
                    players_turn = True
                    AI_playing = False

                elif board[2][2] == '■':
                    board[2][2] = AI_counter
                    print_board(board)
                    players_turn = True
                    AI_playing = False




type_of_game = int(input('single player - press 1, two player - press 2'))
# player decides if they want to play AI or not


still_playing = True

if type_of_game == 1:

    while still_playing == True:

        print('you have chosen single player!')
        single_player()
        playAgain = str(input('would you like to play again? (Y/N)'))

        if playAgain == 'Y' or \
                playAgain == 'y' or \
                playAgain == 'yes' or \
                playAgain == 'Yes':
             still_playing = True
             change_play = str(input('would you like to play single player? (Y/N)'))

             if change_play == 'y':
                type_of_game = 1

             else:
                type_of_game = 2

        elif playAgain == 'N' or \
                playAgain == 'n' or \
                playAgain == 'no' or \
                playAgain == 'No':
            still_playing = False

        else:
            still_playing = False

elif type_of_game == 2:

    while still_playing == True:
        print('you have chosen two player!')
        multi_player()
        playAgain = str(input('would you like to play again? (Y/N)'))

        if playAgain == 'Y' or \
                playAgain == 'y' or \
                playAgain == 'yes' or \
                playAgain == 'Yes':
            still_playing = True
            change_play = str(input('would you like to play single player? (Y/N)'))

            if change_play == 'y':
                type_of_game = 1

            else:
                type_of_game = 2

        elif playAgain == 'N' or \
                playAgain == 'n' or \
                playAgain == 'no' or \
                playAgain == 'No':
            still_playing = False

        else:
            still_playing = False

# runs either single or multiplayer
