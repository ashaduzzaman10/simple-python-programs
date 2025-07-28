# storage file
HISTORY_FILE = "history.txt"


# show file
def showFile():
    try:
        with open(HISTORY_FILE, "r") as file:
            lines = file.readlines()
            if len(lines) == 0:
                print("No history found!")
            else:
                for line in reversed(lines):
                    print(line.strip())
    except FileNotFoundError:
        print("No history file found!")
    except Exception as error:
        print("Something went wrong during file handling: " + str(error))


# clear history
def clearHistory():
    try:
        with open(HISTORY_FILE, "w") as file:
            pass
        print("History cleared!")
    except Exception as error:
        print("Something went wrong during clearing the file: " + str(error))


# save history
def saveHistory(equation, result):
    try:
        with open(HISTORY_FILE, "a") as file:
            file.write(equation + " = " + str(result) + "\n")
    except Exception as error:
        print("Something went wrong during saving the file: " + str(error))


# calculator
def calculatorMachine(userInput):
    try:
        parts = userInput.split()
        if len(parts) != 3:
            print("Invalid input! Use format: number operator number")
            return

        num1 = float(parts[0])
        operation = parts[1]
        num2 = float(parts[2])

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            print("Invalid operator! Use +, -, *, /")
            return

        if result.is_integer():
            result = int(result)

        print("Result:", result)
        saveHistory(userInput, result)

    except Exception as error:
        print("Something went wrong during calculation: " + str(error))


# main function
def main():
    try:
        print("-- Simple Calculator (type history, clear, or exit) --")
        while True:
            userInput = input("Enter calculation or command: ")

            if userInput.lower() == "exit":
                print("Goodbye!")
                break
            elif userInput.lower() == "history":
                showFile()
            elif userInput.lower() == "clear":
                clearHistory()
            else:
                calculatorMachine(userInput)

    except Exception as error:
        print("Something went wrong in the main program: " + str(error))


if __name__ == "__main__":
    main()
