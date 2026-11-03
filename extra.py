import os
from dotenv import load_dotenv

load_dotenv()

DIRECTORY_PATH = os.getenv("PATIENT_FILES_DIR")


print(f"{DIRECTORY_PATH}")
