import random
import pyttsx3
engine = pyttsx3.init()

def speakandprint(str):
    print(str)
    engine.say(str)
    engine.runAndWait()

# QUIZ GAME
def quiz(name,attempt):
    questions = ["What is the primary function of a CPU?", "Which protocol is used for sending emails?", "What is the file extension for a Microsoft Word document?", "What does \"HTML\" stand for in web development?", "What programming language is often used for web development?", "What is the term for a program that replicates itself and spreads to other computers?", " Which programming language is known for its use in data analysis and scientific computing?", "What does \"URL\" stand for?", "In computing, what does \"RAM\" stand for?", "Which company developed the Windows operating system?", " What is the standard protocol used for secure web communication?", "What is the code name of the open-source web browser developed by Mozilla?", "What is the term for a small piece of code that performs a specific task within a larger program?", "What type of software allows users to view web pages on the internet?", "What is the file extension for a compressed archive format commonly used on Windows?"]
    answers = ["processing data", "smtp", "docx", "hypertext markup language", "javascript", "virus", "python", "uniform resource locator", "random access memory", "microsoft", "https", "firefox", "function", "web browser", "zip"]
    speakandprint(f"welcome {name} to the quiz game")
    prize = 0
    i = 0
    while i < attempt:
        if i != 0:
            speakandprint("your next question is\n")
        random_index = random.randint(0, len(questions) - 1)
        speakandprint(questions[random_index])
        speakandprint("your options are:")
        lst_options = []
        for j in range(1,4):
            options = random.randint(0, len(answers) - 1)
            lst_options.append(answers[options])
            if answers[random_index] in lst_options:
                lst_options.append(answers[random.randint(0, len(answers) -1)])
            else:
                lst_options.append(answers[random_index])
        random.shuffle(lst_options)
        print(lst_options)
        k = 1
        for j in lst_options:
            speakandprint(f"{k}. {j}")
            k += 1

        speakandprint("enter your answer : \n")
        a = input()
        if a == answers[random_index]:
            speakandprint("your answer is correct \nyou won 1000 rupees \n ")
            prize = prize + 1000
        else:
            speakandprint("your answer is wrong \nyou lost 500 rupees \n ")
            prize = prize - 500
        i = i+1
    if prize > 0:
        print(name," won: ",prize,"\ncongratulations")
    else:
        print(name," lost: ",prize,"\ntry again")

# ROCK PAPER SCISSORS GAME
def rockpaperscissors(name, n):
    speakandprint(f"Hello {name} to our \n Rock, Paper and Scissors game.")
    output = [
        [0,1,2],
        [2,0,1],
        [1,2,0]
    ]
    a =1
    player_score = 0
    computer_score = 0
    while a <= n:
        user_input = int(input(speakandprint("enter 0 for Rock\nenter 1 for Paper\nenter 2 for Scissors\n")))
        if user_input > 2:
            speakandprint("Enter the correct input")
            continue
        computer_input = random.randint(0,2)
        if output[user_input][computer_input] == 0:
            speakandprint("Match Draw")
        elif output[user_input][computer_input] == 1:
            player_score += 1
            speakandprint(f"{name} wins")
        else:
            computer_score += 1
            speakandprint("computer wins")
        a+=1
    speakandprint(f"score of player {name} : {player_score}")
    speakandprint(f"score of computer : {computer_score}")
    if (player_score < computer_score):
        speakandprint(f"computer wins by {computer_score - player_score}")
    elif(player_score == computer_score):
        speakandprint("It's a draw")
    else:
        speakandprint(f"{name} wins by {player_score - computer_score}")


def SnakeWaterGun(name, n):
    speakandprint(f"Hello {name} to our \n SNAKE, WATER and GUN game.")
    output = [
        [0,1,2],
        [2,0,1],
        [1,2,0]
    ]
    n = int(input("how many chances"))
    a =1
    player_score = 0
    computer_score = 0
    while a <= n:
        user_input = int(input("enter 0 for SNAKE\nenter 1 for WATER\nenter 2 for GUN\n"))
        computer_input = random.randint(0,2)
        if output[user_input][computer_input] == 0:
            speakandprint("Match Draw")
        elif output[user_input][computer_input] == 1:
            player_score += 1
            speakandprint(f"{name} wins")
        else:
            computer_score += 1
            speakandprint("computer wins")
        a+=1
    speakandprint(f"score of player {name} : {player_score}")
    speakandprint(f"score of computer : {computer_score}")
    if (player_score < computer_score):
        speakandprint(f"computer wins by {computer_score - player_score}")
    elif(player_score == computer_score):
        speakandprint("It's a draw")
    else:
        speakandprint(f"{name} wins by {player_score - computer_score}")




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
    speakandprint(f"Welcome {name} to the Tic Tac Toe game.")
    speakandprint("Its the simple 3X3 grid game .")
    speakandprint("You have to enter the row and column number to place your mark.")
    speakandprint("The player who gets 3 marks in a row, column or diagonal wins the game.")
    speakandprint("Lets start the game.")
    choice_symbol = input("Enter your choice of symbol (X or O) : ")
    if choice_symbol == 'X':
        computer = 'O'
        speakandprint("Computer will play with O")
    else:
        computer = 'X'
        speakandprint("Computer will play with X")

    mode = input(speakandprint("Enter the level of difficulty (easy, medium, hard) : "))

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
        speakandprint("Computer's turn")
        turn = 'c'
        computer_row = random.randint(1,3)
        computer_col = random.randint(1,3)
        speakandprint("Computer is thinking...")
        speakandprint(computer_row, computer_col)
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
        
    def index_loo(board,computer_row,computer_col):
        turn = 'c'
        change = 0
        chance = 1
        while turn == 'c':
            if not is_occupied(board, computer_row, computer_col):
                if not is_occupied(board,2,2) and chance == 1:
                    computer_row = 2
                    computer_col = 2
                    change = 1
                    chance = 0
                for i in range(1,4):
                    if board[i][1] == board[i][2] and board[i][1] == choice_symbol and change != 1 and board[i][3] != computer:
                        computer_row = i
                        computer_col = 3
                        change = 1
                        break
                    elif board[i][1] == board[i][3] and board[i][1] == choice_symbol and change != 1 and board[i][2] != computer:
                        computer_row = i
                        computer_col = 2
                        change = 1
                        break
                    elif board[i][2] == board[i][3] and board[i][2] == choice_symbol and change != 1 and board[i][1] != computer:
                        computer_row = i
                        computer_col = 1
                        change = 1
                        break
                    if board[1][i] == board[2][i] and board[1][i] == choice_symbol and change != 1 and board[3][i] != computer:
                        computer_row = 3
                        computer_col = i
                        change = 1
                        break
                    elif board[1][i] == board[3][i] and board[1][i] == choice_symbol and change != 1 and board[2][i] != computer:
                        computer_row = 2
                        computer_col = i
                        change = 1
                        break
                    elif board[2][i] == board[3][i] and board[2][i] == choice_symbol and change != 1 and board[1][i] != computer:
                        computer_row = 1
                        computer_col = i
                        change = 1
                        break
                if board[3][3] == board[1][1] and board[1][1] == choice_symbol and change != 1 and board[2][2] != computer:
                    computer_row = 2
                    computer_col = 2
                    change = 1
                elif board[1][1] == board[2][2] and board[1][1] == choice_symbol and change != 1 and board[3][3] != computer:
                    computer_row = 3
                    computer_col = 3
                    change = 1
                elif board[3][3] == board[2][2] and board[3][3] == choice_symbol and change != 1 and board[2][2] != computer:
                    computer_row = 2
                    computer_col = 2
                    change = 1
                if board[1][3] == board[3][1] and board[1][3] == choice_symbol and change != 1 and board[2][2] != computer:
                    computer_row = 2
                    computer_col = 2
                    change = 1
                elif board[3][1] == board[2][2] and board[3][1] == choice_symbol and change != 1 and board[1][3] != computer:
                    computer_row = 1
                    computer_col = 3
                    change = 1
                elif board[2][2] == board[1][3] and board[3][1] == choice_symbol and change != 1 and board[3][1] != computer:
                    computer_row = 3
                    computer_col = 1
                    change = 1
                if is_occupied(board,2,2) and change != 1:
                    if not is_occupied(board,1,1):
                        computer_row = 1
                        computer_col = 1
                        change = 1
                    elif not is_occupied(board,1,3):
                        computer_row = 1
                        computer_col = 3
                        change = 1
                    elif not is_occupied(board,3,1):
                        computer_row = 3
                        computer_col = 1
                        change = 1
                    elif not is_occupied(board,3,3):
                        computer_row = 3
                        computer_col = 3
                        change = 1
                if not is_occupied(board, computer_row, computer_col):
                    print(computer_row, computer_col)
                    return computer_row, computer_col
                    turn = 'p'
                else:
                    computer_row = random.randint(1,3)
                    computer_col = random.randint(1,3)
                    continue
            else:
                computer_row = random.randint(1,3)
                computer_col = random.randint(1,3) 

    def hard_mode(board):
        speakandprint("Computer's turn")
        speakandprint("Computer is thinking...")
        row, column = index_loo(board,2,2)
        board[row][column] = computer
        print_board(board)

    def medium_mode(board):
        speakandprint("Computer's turn")
        turn = 'c'
        change = 0
        computer_row = random.randint(1,3)
        computer_col = random.randint(1,3)
        speakandprint("Computer is thinking...")
        while turn == 'c':
            if not is_occupied(board, computer_row, computer_col):
                if board[1][1] or board[1][3] or board[3][1] or board[3][3] == choice_symbol and board[2][2] != choice_symbol or computer and change == 1:
                    computer_row = 2
                    computer_col = 2
                if board[1][2] == choice_symbol:
                    if not is_occupied(board,1,1):
                        computer_row =1
                        computer_col = 1
                    elif not is_occupied(board,1,3):
                        computer_row = 1
                        computer_col = 3
                    else:
                        computer_row, computer_col = index_loo(board)
                elif board[2][1] == choice_symbol:
                    if not is_occupied(board,1,1):
                        computer_row =1
                        computer_col = 1
                    elif not is_occupied(board,3,1):
                        computer_row = 1
                        computer_col = 3
                    else:
                        computer_row, computer_col = index_loo(board)
                elif board[3][2] == choice_symbol:
                    if not is_occupied(board,3,1):
                        computer_row =1
                        computer_col = 1
                    elif not is_occupied(board,3,3):
                        computer_row = 1
                        computer_col = 3
                    else:
                        computer_row, computer_col = index_loo(board)
                elif board[2][3] == choice_symbol:
                    if not is_occupied(board,1,3):
                        computer_row =1
                        computer_col = 1
                    elif not is_occupied(board,3,3):
                        computer_row = 1
                        computer_col = 3
                    else:
                        computer_row, computer_col = index_loo(board)
                else:
                    computer_row, computer_col = index_loo(board)

                board[computer_row][computer_col] = computer
            print_board(board)
            turn = 'p'
                

    print_board(board)
    for i in range(1,4):
        for j in range(1,4):
            while board[i][j] == '.':
                row = int(input(speakandprint("Enter row: ")))
                col = int(input(speakandprint("Enter col: ")))
                if row > 3 or col > 3:
                    speakandprint("Enter the row and column number again.\n You have entered the wrong row and column number.")
                    continue
                if board[row][col] == '.':
                    board[row][col] = choice_symbol
                    print_board(board)
                else:
                    speakandprint("Cell is already occupied")
                    speakandprint("Enter the row and column number again.")
                    continue
                if check_draw(board):
                    print_board(board)
                    speakandprint("Draw!")
                    exit()
                elif check_winner(board) == choice_symbol:
                    print_board(board)
                    speakandprint(f"{name} wins!")
                    exit()
                elif check_winner(board) == computer:
                    print_board(board)
                    speakandprint("Computer wins!")
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
                    speakandprint("Draw!")
                    exit()
                elif check_winner(board) == choice_symbol:
                    print_board(board)
                    speakandprint(f"{name} wins!")
                    exit()
                elif check_winner(board) == computer:
                    print_board(board)
                    speakandprint("Computer wins!")
                    exit()

# tic_tac_toe for 2 players

def tic_tac_toe_person(player1, player2):
    speakandprint(f"Welcome {player1} and {player2} to the game of Tic Tac Toe game.")
    speakandprint("Its the simple 3X3 grid game .")
    speakandprint("You have to enter the row and column number to place your mark.")
    speakandprint("The player who gets 3 marks in a row, column or diagonal wins the game.")
    speakandprint("Lets start the game.")
    choice_symbol_1 = input(speakandprint(f"{player1} Enter your choice of symbol (X or O) : "))
    if choice_symbol_1 == 'X':
        choice_symbol_2 = 'O'
        speakandprint(f"{player2} will play with O")
    else:
        choice_symbol_2 = 'X'
        speakandprint(f"{player2} will play with X")
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
            speakandprint("Draw!")
            return True
        elif check_winner(board) == choice_symbol_1:
            print_board(board)
            speakandprint(f"{player1} wins!")
            return True
        elif check_winner(board) == choice_symbol_2:
            print_board(board)
            speakandprint(f"{player2} wins!")
            return True


    print_board(board)
    for i in range(1,4):
        for j in range(1,4):
            while board[i][j] == '.':
                turn = 'p1'
                while turn == 'p1':
                    row = int(input(speakandprint("Enter row: ")))
                    col = int(input(speakandprint("Enter col: ")))
                    if row > 3 or col > 3:
                        speakandprint("Enter the row and column number again.\n You have entered the wrong row and column number.")
                        continue
                    if board[row][col] == '.':
                        board[row][col] = choice_symbol_1
                        print_board(board)
                        turn = 'p2'
                    else:
                        speakandprint("Cell is already occupied")
                        speakandprint("Enter the row and column number again.")
                        continue

                if check(board):
                    exit()

                else:
                    speakandprint(f"{player2} turn")
                    while turn == 'p2':
                        row = int(input(speakandprint("Enter row: ")))
                        col = int(input(speakandprint("Enter col: ")))
                        if row > 3 or col > 3:
                            speakandprint("Enter the row and column number again.\n You have entered the wrong row and column number.")
                            continue
                        if board[row][col] == '.':
                            board[row][col] = choice_symbol_2
                            print_board(board)
                            turn = 'p1'
                        else:
                            speakandprint("Cell is already occupied")
                            speakandprint("Enter the row and column number again.")
                            continue   
                if check(board):
                    exit()

name = input(speakandprint("enter your name : \n"))
speakandprint(f"welcome {name} to the world of games. We have many games for you to play")
speakandprint("choose the game you want to play")
choice = 0
while True:
    choice= input(speakandprint("1. Quiz Game \n2. Rock Paper Scissors \n3. Tic Tac Toe \n4. Snake Water Gun \n5. Exit"))
    speakandprint(f"You choice is : {choice}" )
    if choice == '1':
        speakandprint("enter number of attempts : \n")
        attempt = int(input())
        quiz(name,attempt)
    elif choice == '2':
        speakandprint("enter number of attempts : \n")
        attempt = int(input())
        rockpaperscissors(name,attempt)
    elif choice == '3':
        choice_in = input(speakandprint("Do you want to play with computer or with another player"))
        if choice_in == 'computer':
            tic_tac_toe_computer(name)
        else:
            player2 = input(speakandprint("enter the name of player 2 : "))
            tic_tac_toe_person(name,player2)
    elif choice == '4':
        speakandprint("enter number of attempts : \n")
        attempt = int(input())
        SnakeWaterGun(name,attempt)
    elif choice == '5':
        speakandprint("Thank you for playing. Have a great day")
        exit()

# save user data in a databse for future use, we will keep a system of money every user will get 1000 rs and to play a game he/she had to pay 100 rs, for every win 500rs will add in his account 
# if his/her balance will come to 0 he had to recharge his account via admin's account