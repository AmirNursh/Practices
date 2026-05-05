with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

with open("sample.txt", "r") as file:
    print(file.readline())

with open("sample.txt", "r") as file:
    lines = file.readlines()
    print(lines)