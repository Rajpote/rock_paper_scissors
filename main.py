import random

def get_choices():
  player_choice = input("enter a choice:")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player, computer):
    print(f"you chose {player} ,computer chose {computer}")
    if player == computer:
     print("tie")
    elif player == "rock":
     if computer == "scissors":
        print("rock smashes scissors you win")
     else:
        print("paper smashes rock you lose")
    elif player == "paper":
     if computer == "rock":
        print("paper smashes rocks you win")
     else:
        print("scissors smashes paper you lose")
    elif player == "scissors":
     if computer == "paper":
        print("scissors smashes paper you win")
     else:
        print("rock smashes scissors you lose")

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)