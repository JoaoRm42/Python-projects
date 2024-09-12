"""This is a to do list program made by https://github.com/JoaoRm42"""

import os
import time
from sys import platform

def check_platform():
    """Checks what operating system you are currently using and clears your terminal"""
    if platform == "linux" or platform == "linux2":
        os.system("clear")
    elif platform == "win32":
        os.system("cls")

def menu_text():
    """Prints the intro Text"""
    check_platform()
    print ("Welcome to your to do list")
    print ("1. Add")
    print ("2. Show")
    print ("3. Remove")
    print ("4. Exit\n")

def outro():
    """Prints outro text when leaving"""
    check_platform()
    print("Thank you for using me")

def add_task():
    """Add task to your list"""
    check_platform()
    file_name = input("Name your file\n|> ")
    file_name = file_name + ".txt"
    try:
        file = open(file_name, "r")
    except:
        check_platform()
        file_create = input("Your file doesn't exist\nWant to create it?\nY | N\n|> ")
        if file_create == "Y" or file_create == "y":
            open(file_name, "x")
        else:
            return 1
    check_platform()
    task = input("What do you wish to add to your " + file_name + "?\n|> ")
    file = open(file_name, "a")
    with open(file_name, "r") as f:
        lines = f.readlines()
        num_lines = len(lines) + 1
    file.write(task + "\n")
    print(num_lines)
    file.close()

def show_tasks_from_file():
    """Opens file and prints its content"""
    check_platform()
    try:
        file_name = input("Name your file\n|> ")
        file_name = file_name + ".txt"
        file = open(file_name, "r")
        check_platform()
        with open(file_name, "r") as f:
            lines = f.readlines()
        for index, task in enumerate(lines):
            print(f"{index}. {task}", end="")
        print()
        input("Exit?\n|> ")
    except:
        print("File doesn't exist!")
        time.sleep(2)
        return 1

def remove_task_from_file():
    """Removes string from file by the index"""
    check_platform()
    try:
        file_name = input("Name your file\n|> ")
        file_name = file_name + ".txt"
        file = open(file_name, "r")
        check_platform()

        with open(file_name, "r") as f:
            lines = f.readlines()
        for index, task in enumerate(lines):
            print(f"{index}. {task}", end="")
        print()
        answer = input("Which task would you like to remove?\nRemove by index!\n(Example: 5. Build frontend, you type only 5)\n|> ")
        try:
            index_to_remove = int(answer)
            if 0 <= index_to_remove < len(lines):
                del lines[index_to_remove]
            else:
                print("Index doesn't exist")
                time.sleep(2)
                return 1
        except ValueError:
            print("Invalid index. Please enter a number.")
            time.sleep(2)
            return 1

        with open(file_name, "w") as f:
            f.writelines(lines)

        print("Task removed successfully.")
        time.sleep(2)

    except FileNotFoundError:
        print("File doesn't exist!")
        time.sleep(2)
        return 1
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(2)
        return 1

def menu():
    """Menu of the choices to be done inside program"""
    while 1:
        menu_text()
        answer = input("|> ")
        if answer == '1':
            add_task()
        elif answer == '2':
            show_tasks_from_file()
        elif answer == '3':
            remove_task_from_file()
        elif answer == '4':
            break

def main():
    menu()
    outro()


if __name__ == "__main__":
    main()
