import random

gameItemList = ["rock", "paper", "scissor"]

userInput = input("enter your move : (Rock ,Paper, Scissor ) = ")

computerChoice = random.choice(gameItemList)

print(f"User choice is : {userInput} , and computer choice is : {computerChoice}")

# game logic

if userInput == computerChoice:
    print("both choice are same value = Match tie ")

elif userInput == "rock":
    if computerChoice == "paper":
        print("paper cover rock = computer win ")
    else:
        print("rock smashes scissor = You win ")

elif userInput == "paper":
    if computerChoice == "scissor":
        print("scissor cuts paper , computer win ")
    else:
        print("paper cover scissor , you win ")

elif userInput == "scissor":
    if computerChoice == "paper":
        print("scissor cuts paper ,you win ")
    else:
        print("rock smashes scissor ,computer win ")
