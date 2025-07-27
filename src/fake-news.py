# 1 -> import the random module

import random


# 2 -> create subject

subjects = [
    "Sah sharuk khan ",
    "virat koholi ",
    "nirmola sitaram ",
    "a group of mumbai ",
    "a cat from dhaka ",
    "student form DIu ",
    "auto rickshow form gulsan ",
]

actions = [
    "launces ",
    "cancels ",
    "dances with ",
    "eats ",
    "declar war on ",
    "orders ",
    "celebrates ",
]


places_or_things = [
    "at red fort ",
    "in mumbai local trains",
    "a plat of tea",
    "inside parliaments",
    "at rangpur ",
    "during crickets match ",
    "at bosundhora ",
]


# 3 -> start the heading generation loop
while True:
    subjects = random.choice(subjects)
    actions = random.choice(actions)
    places_or_things = random.choice(places_or_things)

    headline = f"BREAKING NEWS : {subjects}{actions}{places_or_things}"
    print("\n " + headline)

    userInput = (
        input("\n do you want to generate another headline ? (yes/no)").strip().lower()
    )
    if userInput == "no":
        break

# 4 -> print good bye to the user

print("\n thanks for using fake news generator ")
