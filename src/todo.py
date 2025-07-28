
# logic 
def taskManager():
    print("---------------------------------------")
    print("*** welcome to the TASK Manager APP ***")
    print("---------------------------------------")
    tasks = []

    while True:
        try:
            totalTask = int(input("enter how many tasks you want to add : "))
            break
        except ValueError:
            print("Please enter a valid number!")

    for value in range(1, totalTask + 1):
        taskName = input(f"Enter task {value}: ")
        tasks.append(taskName)

    print(f"your tasks for today is : {tasks}")

    while True:
        try:
            operation = int(
                input(
                    "Enter your command : 1 - add \n 2 - update\n 3 - delete \n 4 - view \n 5 - exit "
                )
            )
        except ValueError:
            print("Please enter a valid number (1-5)!")
            continue

        if operation == 1:
            add = input("enter your task  :: ")
            tasks.append(add)
            print(f"task {add} has been added successfully")

        elif operation == 2:
            updatedValue = input("enter the task name for update ::")
            if updatedValue in tasks:
                update = input("update with new task :: ")
                updateOperation = tasks.index(updatedValue)
                tasks[updateOperation] = update
                print(f"your task has been updated :: {update}")
            else:
                print("Task not found!")

        elif operation == 3:
            deleteTask = input("enter the task name to delete :: ")
            if deleteTask in tasks:
                tasks.remove(deleteTask)
                print(f"task {deleteTask} has been deleted successfully")
            else:
                print("Task not found!")

        elif operation == 4:
            print(f"Your current tasks: {tasks}")

        elif operation == 5:
            print("Goodbye!")
            break

        else:
            print("Invalid operation! Please choose 1-5.")


#  run the program
if __name__ == "__main__":
    taskManager()
