import shutil
import os

os.makedirs("destination", exist_ok=True)

# Move file
if os.path.exists("sample.txt"):
    shutil.move("sample.txt", "destination/sample.txt")
    print("File moved.")