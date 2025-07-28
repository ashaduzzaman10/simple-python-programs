import os


# file creation
def createFile(fileName):
    try:
        with open(fileName, "x") as file:
            print(f"File '{fileName}' created successfully.")
    except FileExistsError:
        print(f"File '{fileName}' already exists!")
    except Exception as error:
        print(f"An error occurred during file creation: {error}")


# display file
def displayAllFiles():
    try:
        files = os.listdir()
        if not files:
            print("No files found!")
        else:
            print("Files in directory:")
            for file in files:
                print(file)
    except Exception as error:
        print(f"Error while displaying files: {error}")


# delete file
def deleteFile(fileName):
    try:
        os.remove(fileName)
        print(f"'{fileName}' has been deleted successfully.")
    except FileNotFoundError:
        print(f"'{fileName}' not found!")
    except Exception as error:
        print(f"Error deleting file: {error}")


# read file
def readFile(fileName):
    try:
        with open(fileName, "r") as file:
            content = file.read()
            print(f"Content of '{fileName}':\n{content}")
    except FileNotFoundError:
        print(f"'{fileName}' does not exist!")
    except Exception as error:
        print(f"Error reading file: {error}")


# edit file
def editFile(fileName):
    try:
        with open(fileName, "a") as file:
            content = input("Enter data to append: ")
            file.write(content + "\n")
            print(f"Data added successfully to '{fileName}'.")
    except FileNotFoundError:
        print(f"'{fileName}' does not exist!")
    except Exception as error:
        print(f"Error editing file: {error}")


# logic
def main():
    while True:
        print("\nFile Management App")
        print("1: Create File")
        print("2: View All Files")
        print("3: Delete File")
        print("4: Read File")
        print("5: Edit File")
        print("6: Exit")
        choice = input("Enter your choice (1-6): ")

        match choice:
            case "1":
                fileName = input("Enter the file name to create: ")
                createFile(fileName)
            case "2":
                displayAllFiles()
            case "3":
                fileName = input("Enter the file name to delete: ")
                deleteFile(fileName)
            case "4":
                fileName = input("Enter the file name to read: ")
                readFile(fileName)
            case "5":
                fileName = input("Enter the file name to edit: ")
                editFile(fileName)
            case "6":
                print("Closing the app...")
                break
            case _:
                print("Invalid choice!")


# run
if __name__ == "__main__":
    main()


# logic using conditional
#             fileName = input("enter the file name to create  : ")
#             createFile(fileName)

#         elif choice == "2":
#             displayAllFiles()

#         elif choice == "3":
#             fileName = input("enter the file name to delete  : ")
#             deleteFile(fileName)

#         elif choice == "4":
#             fileName = input("enter the file name to read  : ")
#             readFile(fileName)

#         elif choice == "5":
#             fileName = input("enter the file name to edit  : ")
#             editFile(fileName)

#         elif choice == "6":
#             print("Closing the APP..........")
#             break
#         else:
#             print("invalid syntax ")
