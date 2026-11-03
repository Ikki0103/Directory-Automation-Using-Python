import os
import tkinter as tk

DIRECTORY_PATH = "D:/Tirzuh/Justinne Khrey abad Things/PatientFiles"


def create_directory(dir_name):
    directory_name = str(dir_name)
    full_path = os.path.join(DIRECTORY_PATH, directory_name)

    if not os.path.exists(full_path):
        os.makedirs(full_path, exist_ok=True)
        print(f"Directory '{directory_name}' created Successfully")

    else:
        print(f"Directory '{full_path}' already Exists!")


def search_directory(dir_name):
    directory_name = str(dir_name)
    full_path = os.path.join(DIRECTORY_PATH, directory_name)

    if not os.path.exists(full_path):
        print(f"Directory '{directory_name}' Not Exists")
    else:
        is_goto_file = input(
            f"Directory '{directory_name}' already Exists! Do you want to open the path? Y/N: ")
        if is_goto_file.strip().upper() == 'Y':
            os.startfile(full_path)


def main():
    dir_name = ""
    while True:
        try:
            print("*****Ikki Automation Tools*****\n")
            print("[1]Create Directory\n[2]Search Directory\n[3]Exit")
            choice = int(input("Enter Choice: "))
            if choice == 4:
                print('Program Ended')
                choice = None
                break
            if not dir_name:
                dir_name = input("Enter Directory Name: ")
                if not dir_name:
                    print(f"Please Enter Directory Name")
                    continue

            # Choices
            match choice:
                case 1:
                    create_directory(dir_name)
                case 2:
                    search_directory(dir_name)
                case 3:
                    print("Goodbye!")
                    break

        except ValueError:
            print("Invalid Input\n")


if __name__ == "__main__":
    main()
