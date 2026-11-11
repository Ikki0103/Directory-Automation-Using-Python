
import os
from pathlib import Path
import subprocess
from dotenv import load_dotenv

load_dotenv()

DIRECTORY_PATH = None

# Function for validating Directory path
def validate_path():
    global DIRECTORY_PATH

    patient_dir = os.getenv("PATIENT_FILES_DIR")

    if not patient_dir:
        raise ValueError("PATIENT_FILES_DIR is not configured in .env")

    DIRECTORY_PATH = Path(patient_dir)

    if not DIRECTORY_PATH.is_dir():
        raise NotADirectoryError(
            f"Invalid patient directory: {DIRECTORY_PATH}"
        )

# Function for validating user-entered directory names
def get_directory_path(dir_name):
    name = Path(str(dir_name))

    if name.is_absolute() or len(name.parts) != 1 or name.name in (".", ".."):
        raise ValueError("Invalid directory name.")

    return DIRECTORY_PATH / name


# Function for creating new directory
def create_directory(dir_name):
    directory_name = str(dir_name)
    full_path = get_directory_path(dir_name)

    clear_screen()

    if not full_path.exists():
        full_path.mkdir(parents=True, exist_ok=True)
        print(f"Directory '{directory_name}' created Successfully")
    else:
        print(f"Directory '{full_path}' already Exists!")


# Function for searching if the directory exists
def search_directory(dir_name):
    directory_name = str(dir_name)
    full_path = get_directory_path(dir_name)

    clear_screen()

    if not full_path.is_dir():
        print(f"Directory '{directory_name}' Not Exists")
    else:
        is_goto_file = input(
            f"Directory '{directory_name}' Exists! Do you want to open the path? Y/N: "
        )

        if is_goto_file.strip().upper() == 'Y':
            os.startfile(full_path)


# Function in opening the current selected directory
def open_directory(dir_name):
    directory_name = str(dir_name)
    full_path = get_directory_path(dir_name)

    clear_screen()

    if not full_path.is_dir():
        print(f"Directory '{directory_name}' Does not Exists!!")
    else:
        os.startfile(full_path)


# Function for clearing previous process from terminal
def clear_screen():
    subprocess.run(
        ['cmd', '/c', 'cls'] if os.name == 'nt' else ['clear'],
        check=False
    )


def main():
    dir_name = ""

    while True:
        try:
            print("*****Ikki Automation Tools*****\n")
            print(
                "[1]Create Directory\n"
                "[2]Search Directory\n"
                "[3]Open Directory\n"
                "[4]Exit"
            )

            choice = int(input("Enter Choice: "))

            if not dir_name:
                dir_name = input("Enter Directory Name: ")

                if not dir_name:
                    print("Please Enter Directory Name")
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
                case _:
                    print("Invalid Choice...")
        except ValueError:
            print("Invalid Input...\n")


if __name__ == "__main__":
    try:
        validate_path()
        main()
    except (ValueError, NotADirectoryError) as e:
        print(f"Configuration Error: {e}")
        input("Press Enter to exit...")
