import shutil
import os

# Append text
with open("sample.txt", "a") as file:
    file.write("New line added.\n")

# Copy file
shutil.copy("sample.txt", "backup_sample.txt")
print("Backup created.")

# Delete file safely
if os.path.exists("backup_sample.txt"):
    os.remove("backup_sample.txt")
    print("Backup deleted.")
else:
    print("File does not exist.")