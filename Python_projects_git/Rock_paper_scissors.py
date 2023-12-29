import random
choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
player = False
cpu_score = 0
player_score = 0
while True:
    player = input("Rock, Paper, Scissors!").capitalize()
    if player == computer:
        print("tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("you lose", computer, "covers", player)
            cpu_score += 1
        else:
            print("you won", player, "smashes", computer)
            player_score += 1
    elif player == "Paper":
        if computer == "Scissors":
            print("you loses", computer, "cut", player)
            cpu_score += 1
        else:
            print("you won", player, "covers", computer)
            player_score += 1
    elif player == "Scissors":
        if computer == "Rock":
            print("you loses", computer, "smashes", player)
            cpu_score += 1
        else:
            print("you won", player, "cut", computer)
            player_score += 1
    elif player == 'End':
        print("Final Scores:")
        print(f"CPU:{cpu_score}")
        print(f"Player:{player_score}")
        break
        


