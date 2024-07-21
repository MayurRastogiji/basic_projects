import random
name = str(input("Enter your name:"))
print(f"Hello {name} to our \n SNAKE, WATER and GUN game.")
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
        print("Match Draw")
    elif output[user_input][computer_input] == 1:
        player_score += 1
        print(f"{name} wins")
    else:
        computer_score += 1
        print("computer wins")
    a+=1
print(f"score of player {name} : {player_score}")
print(f"score of computer : {computer_score}")
if (player_score < computer_score):
    print(f"computer wins by {computer_score - player_score}")
elif(player_score == computer_score):
    print("It's a draw")
else:
    print(f"{name} wins by {player_score - computer_score}")