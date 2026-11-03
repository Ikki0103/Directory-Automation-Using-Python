import os
from dotenv import load_dotenv

load_dotenv()

DIRECTORY_PATH = os.getenv("PATIENT_FILES_DIR")


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
            f"Directory '{directory_name}' Exists! Do you want to open the path? Y/N: ")
        if is_goto_file.strip().upper() == 'Y':
            os.startfile(full_path)


def open_directory(dir_name):
    directory_name = str(dir_name)
    full_path = os.path.join(DIRECTORY_PATH, directory_name)

    if not os.path.exists(full_path):
        print(f"Directory {directory_name} Not Found!!")
    else:
        os.startfile(full_path)


def main():
    dir_name = ""
    while True:
        try:
            print("*****Ikki Automation Tools*****\n")
            print(
                "[1]Create Directory\n[2]Search Directory\n[3]Open Directory\n[4]Exit")
            choice = int(input("Enter Choice: "))
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
                    open_directory(dir_name)
                case 4:
                    print("Goodbye!")
                    break

            # if choice == 3:
            #     print('Program Ended')
            #     choice = None
            #     break
            # if not dir_name:
            #     dir_name = input("Enter Directory Name: ")
            #     if not dir_name:
            #         print(f"Please Enter Directory Name")
            #         continue
        except ValueError:
            print("Invalid Input\n")


if __name__ == "__main__":
    main()
