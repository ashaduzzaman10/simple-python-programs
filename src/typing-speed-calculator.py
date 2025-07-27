from time import *
import random as r


# calculate mistakes
def typeMistake(paragraphText, userText):
    error = 0
    for key in range(len(paragraphText)):
        try:
            if paragraphText[key] != userText[key]:
                error += 1
        except:
            error += 1
    return error


# calculate typing speed (characters per second)
def timeCalculation(startTime, endTime, userInput):
    timeDelay = endTime - startTime
    timeRoundUp = round(timeDelay, 2)
    typeSpeed = len(userInput) / timeRoundUp
    return round(typeSpeed, 2)


# default text options
text_samples = [
    "the quick brown fox jumps over the lazy dog",
    "share your knowledge",
    "keep humble and stay calm",
    "we are at the end of the test",
]

# display and logic
while True:
    text_to_type = r.choice(text_samples)
    print("-----------**************** TYPING TEST *****************----------------")
    print(text_to_type)
    print()

    startTime = time()
    user_input = input("Enter: ")
    endTime = time()

    speed = timeCalculation(startTime, endTime, user_input)
    errors = typeMistake(text_to_type, user_input)

    print(f"\nSpeed: {speed} characters/sec")
    print(f"Errors: {errors}\n")

    retry = input(" do you want to try another test? (y/n): ").strip().lower()
    if retry != "y":
        print("\n thank you for visiting!")
        break
