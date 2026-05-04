# json.py

import json  # module for working with JSON data

# ---------- Reading JSON ----------

# Open and read JSON file
with open("sample-data.json", "r") as file:
    data = json.load(file)  # convert JSON into Python dictionary

# Access some fields safely using .get()
print("Name:", data.get("name"))
print("Age:", data.get("age"))

# ---------- Modifying JSON ----------

# Add a new field to the dictionary
data["updated"] = True

# ---------- Writing JSON ----------

# Write updated data into a new file
with open("updated-data.json", "w") as file:
    json.dump(data, file, indent=4)  # indent makes output formatted nicely

print("Updated JSON saved to updated-data.json")
