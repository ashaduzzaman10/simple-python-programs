# sum
def sum(a, b, c):
    return a + b + c


# board view
def printBoard(xState, zState):
    zero = "X" if xState[0] else ("O" if zState[0] else 0)
    one = "X" if xState[1] else ("O" if zState[1] else 1)
    two = "X" if xState[2] else ("O" if zState[2] else 2)
    three = "X" if xState[3] else ("O" if zState[3] else 3)
    four = "X" if xState[4] else ("O" if zState[4] else 4)
    five = "X" if xState[5] else ("O" if zState[5] else 5)
    six = "X" if xState[6] else ("O" if zState[6] else 6)
    seven = "X" if xState[7] else ("O" if zState[7] else 7)
    eight = "X" if xState[8] else ("O" if zState[8] else 8)

    print(f" | {zero} | {one} | {two} |")
    print(f" | - | - | - |")
    print(f" | {three} | {four} | {five} |")
    print(f" | - | - | - |")
    print(f" | {six} | {seven} | {eight} |")


# logic
def checkWin(xState, zState):
    Wins = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    for win in Wins:
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            print("X won the game!")
            return 1
        if sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            print("O won the game!")
            return 0
    return -1


if __name__ == "__main__":
    xState = [0] * 9
    zState = [0] * 9
    turn = 1  # 1 for X, 0 for O
    print("Welcome to Tic Tac Toe!")

    while True:
        printBoard(xState, zState)
        if turn == 1:
            print("X's turn")
            value = int(input("Enter position (0-8): "))
            xState[value] = 1
        else:
            print("O's turn")
            value = int(input("Enter position (0-8): "))
            zState[value] = 1

        cWin = checkWin(xState, zState)
        if cWin != -1:
            printBoard(xState, zState)
            print("Match over!")
            break

        turn = 1 - turn
