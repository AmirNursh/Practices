import os

# Create directory
os.makedirs("test_folder/subfolder", exist_ok=True)

# Current directory
print("Current directory:", os.getcwd())

# List files and folders
print("Files and folders:")
print(os.listdir("."))

# Remove directory
os.rmdir("test_folder/subfolder")