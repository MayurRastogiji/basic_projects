# TIC TAC TOE GAME
"""
There are two ways to playa game of Tic Tac Toe.
one is to play with computer and other is to play with another player.
if you want to play with computer then you have to call the function tic_tac_toe(name)
if you want to play with another player then you have to call the function tic_tac_toe(player1, player2)
if you choose to play with computer then you have to selecr your level of difficulty.
there are three levels of difficulty.
1. Easy
    where computer will play randomly.
2. Medium
    where computer will play randomly but it always stops the player from winning.
3. Hard
    where computer will play randomly but it always stops the player from winning and tries to win the game., it had some of its own techiniques ot win the game as well."""


import random

# tic_tac_toe for 1 player
def tic_tac_toe_computer(name):
    print(f"Welcom {name} to the game of Tic Tac Toe game.")
    print("Its the simple 3X3 grid game .")
    print("You have to enter the row and column number to place your mark.")
    print("The player who gets 3 marks in a row, column or diagonal wins the game.")
    print("Lets start the game.")
    choice_symbol = input("Enter your choice of symbol (X or O) : ")
    if choice_symbol == 'X':
        computer = 'O'
        print("Computer will play with O")
    else:
        computer = 'X'
        print("Computer will play with X")

    mode = input("Enter the level of difficulty (easy, medium, hard) : ")

    board = [
        [' ','1','2','3'],
        ['1','.','.','.'],
        ['2','.','.','.'],
        ['3','.','.','.']
    ]

    def print_board(board):
        for i in range(4):
            for j in range(4):
                print(board[i][j], end = " ")
            print()
    def check_winner(board):
        for i in range(1,4):
            if board[i][1] == board[i][2] == board[i][3] and board[i][1] != '.':
                return board[i][1]
            if board[1][i] == board[2][i] == board[3][i] and board[1][i] != '.':
                return board[1][i]
        if board[3][3] == board[1][1] == board[2][2] and board[1][1] != '.':
            return board[1][1]
        if board[1][3] == board[2][2] == board[3][1] and board[1][3] != '.':
            return board[1][3]
        else:
            return None
    def check_draw(board):
        if check_winner(board) == None:
            for i in range(4):
                for j in range(4):
                    if board[i][j] == '.':
                        return False
            return True
    def easy_mode(board):
        print("Computer's turn")
        turn = 'c'
        computer_row = random.randint(1,3)
        computer_col = random.randint(1,3)
        print("Computer is thinking...")
        print(computer_row, computer_col)
        while turn == 'c':
            if board[computer_row][computer_col] == '.':
                
                board[computer_row][computer_col] = computer
                print_board(board)
                turn = 'p'
            else:
                computer_row = random.randint(1,3)
                computer_col = random.randint(1,3)
                continue

    def is_occupied(board, row, col):
        if board[row][col] == '.':
            return False
        else:
            return True

    def medium_mode(board):
        print("Computer's turn")
        turn = 'c'
        change = 0
        computer_row = random.randint(1,3)
        computer_col = random.randint(1,3)
        print("Computer is thinking...")
        while turn == 'c':
            if not is_occupied(board, computer_row, computer_col):
                for i in range(1,4):
                    if board[i][1] == board[i][2] and board[i][1] == choice_symbol and change != 1 and board[i][3] != computer:
                        computer_row = i
                        computer_col = 3
                        change = 1
                        break
                    elif board[i][1] == board[i][3] and board[i][1] == choice_symbol and change != 1 and board[i][3] != computer:
                        computer_row = i
                        computer_col = 2
                        change = 1
                        break
                    elif board[i][2] == board[i][3] and board[i][2] == choice_symbol and change != 1 and board[i][3] != computer:
                        computer_row = i
                        computer_col = 1
                        change = 1
                        break
                    if board[1][i] == board[2][i] and board[1][i] == choice_symbol and change != 1 and board[i][3] != computer:
                        computer_row = 3
                        computer_col = i
                        change = 1
                        break
                    elif board[1][i] == board[3][i] and board[1][i] == choice_symbol and change != 1 and board[i][3] != computer:
                        computer_row = 2
                        computer_col = i
                        change = 1
                        break
                    elif board[2][i] == board[3][i] and board[2][i] == choice_symbol and change != 1 and board[i][3] != computer:
                        computer_row = 1
                        computer_col = i
                        change = 1
                        break
                if board[3][3] == board[1][1] and board[1][1] == choice_symbol and change != 1 and board[i][3] != computer:
                    computer_row = 2
                    computer_col = 2
                    change = 1
                elif board[1][1] == board[2][2] and board[1][1] == choice_symbol and change != 1 and board[i][3] != computer:
                    computer_row = 3
                    computer_col = 3
                    change = 1
                elif board[3][3] == board[2][2] and board[3][3] == choice_symbol and change != 1 and board[i][3] != computer:
                    computer_row = 2
                    computer_col = 2
                    change = 1
                if board[1][3] == board[3][1] and board[1][3] == choice_symbol and change != 1 and board[i][3] != computer:
                    computer_row = 2
                    computer_col = 2
                    change = 1
                elif board[3][1] == board[2][2] and board[3][1] == choice_symbol and change != 1 and board[i][3] != computer:
                    computer_row = 1
                    computer_col = 3
                    change = 1
                elif board[3][1] == board[1][3] and board[3][1] == choice_symbol and change != 1 and board[i][3] != computer:
                    computer_row = 2
                    computer_col = 2
                    change = 1
                if not is_occupied(board, computer_row, computer_col):
                    print(computer_row, computer_col)
                    board[computer_row][computer_col] = computer
                    print_board(board)
                    turn = 'p'
                else:
                    computer_row = random.randint(1,3)
                    computer_col = random.randint(1,3)
                    continue
            else:
                computer_row = random.randint(1,3)
                computer_col = random.randint(1,3) 
    def hard_mode(board):
        print("This mode will come soon")

    print_board(board)
    for i in range(1,4):
        for j in range(1,4):
            while board[i][j] == '.':
                row = int(input("Enter row: "))
                col = int(input("Enter col: "))
                if row > 3 or col > 3:
                    print("Enter the row and column number again.\n You have entered the wrong row and column number.")
                    continue
                if board[row][col] == '.':
                    board[row][col] = choice_symbol
                    print_board(board)
                else:
                    print("Cell is already occupied")
                    print("Enter the row and column number again.")
                    continue
                if check_draw(board):
                    print_board(board)
                    print("Draw!")
                    exit()
                elif check_winner(board) == choice_symbol:
                    print_board(board)
                    print(f"{name} wins!")
                    exit()
                elif check_winner(board) == computer:
                    print_board(board)
                    print("Computer wins!")
                    exit()
                else:
                    if mode == 'easy':
                        easy_mode(board)
                    elif mode == 'medium':
                        medium_mode(board)
                    elif mode == 'hard':
                        hard_mode(board)
                if check_draw(board):
                    print_board(board)
                    print("Draw!")
                    exit()
                elif check_winner(board) == choice_symbol:
                    print_board(board)
                    print(f"{name} wins!")
                    exit()
                elif check_winner(board) == computer:
                    print_board(board)
                    print("Computer wins!")
                    exit()

# tic_tac_toe for 2 players

def tic_tac_toe_person(player1, player2):
    print(f"Welcome {player1} and {player2} to the game of Tic Tac Toe game.")
    print("Its the simple 3X3 grid game .")
    print("You have to enter the row and column number to place your mark.")
    print("The player who gets 3 marks in a row, column or diagonal wins the game.")
    print("Lets start the game.")
    choice_symbol_1 = input(f"{player1} Enter your choice of symbol (X or O) : ")
    if choice_symbol_1 == 'X':
        choice_symbol_2 = 'O'
        print(f"{player2} will play with O")
    else:
        choice_symbol_2 = 'X'
        print(f"{player2} will play with X")
    board = [
        [' ','1','2','3'],
        ['1','.','.','.'],
        ['2','.','.','.'],
        ['3','.','.','.']
    ]
    def print_board(board):
        for i in range(4):
            for j in range(4):
                print(board[i][j], end = " ")
            print()
    def check_winner(board):
        for i in range(1,4):
            if board[i][1] == board[i][2] == board[i][3] and board[i][1] != '.':
                return board[i][1]
            if board[1][i] == board[2][i] == board[3][i] and board[1][i] != '.':
                return board[0][i]
        if board[3][3] == board[1][1] == board[2][2] and board[1][1] != '.':
            return board[1][1]
        if board[1][3] == board[3][3] == board[3][1] and board[1][3] != '.':
            return board[1][3]
        else:
            return None
    def check_draw(board):
        if check_winner(board) == None:
            for i in range(4):
                for j in range(4):
                    if board[i][j] == '.':
                        return False
            return True
    def check(board):
        if check_draw(board):
            print_board(board)
            print("Draw!")
            return True
        elif check_winner(board) == choice_symbol_1:
            print_board(board)
            print(f"{player1} wins!")
            return True
        elif check_winner(board) == choice_symbol_2:
            print_board(board)
            print(f"{player2} wins!")
            return True


    print_board(board)
    for i in range(1,4):
        for j in range(1,4):
            while board[i][j] == '.':
                turn = 'p1'
                while turn == 'p1':
                    row = int(input("Enter row: "))
                    col = int(input("Enter col: "))
                    if row > 3 or col > 3:
                        print("Enter the row and column number again.\n You have entered the wrong row and column number.")
                        continue
                    if board[row][col] == '.':
                        board[row][col] = choice_symbol_1
                        print_board(board)
                        turn = 'p2'
                    else:
                        print("Cell is already occupied")
                        print("Enter the row and column number again.")
                        continue

                if check(board):
                    exit()

                else:
                    print(f"{player2} turn")
                    while turn == 'p2':
                        row = int(input("Enter row: "))
                        col = int(input("Enter col: "))
                        if row > 3 or col > 3:
                            print("Enter the row and column number again.\n You have entered the wrong row and column number.")
                            continue
                        if board[row][col] == '.':
                            board[row][col] = choice_symbol_2
                            print_board(board)
                            turn = 'p1'
                        else:
                            print("Cell is already occupied")
                            print("Enter the row and column number again.")
                            continue   
                if check(board):
                    exit()
tic_tac_toe_computer("Rahul")