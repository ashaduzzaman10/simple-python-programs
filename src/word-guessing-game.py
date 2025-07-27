import random

# action word 
easyWord = ["apple", "banana", "tiger", "money", "bangladesh"]

mediumWord = ["python", "javascript", "tomato", "computer", "campus"]

hardWord = ["university", "school", "dhaka", "badda", "mountain"]

print("Welcome to the password gassing game ")
print("Choose the difficulty level : easy ,medium,hard ")

#counting level 

level = input("Enter difficulty level : ").lower()
if level == "easy":
    secret = random.choice(easyWord)
elif level == "medium":
    secret = random.choice(mediumWord)
elif level == "hard":
    secret = random.choice(hardWord)
else:
    print("invalid choice ! default normal level (easy)")
    secret = random.choice(easyWord)


attempts = 0
print("\n guess the secret password ")

#gassing logic 
while True:
    guess = input("enter the input ")
    attempts += 1

    if guess == secret:
        print(f"congrats , Your guess it in {attempts} attempts ")
        break

    hint = ""
    for value in range(len(secret)):
        if value < len(guess) and guess[value] == secret[value]:
            hint += guess[value]
        else:
            hint += "_"
        print("hint : " + hint)

print("game over !")
