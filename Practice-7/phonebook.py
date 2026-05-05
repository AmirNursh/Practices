import csv
from connect import connect


# Create table
def create_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            phone VARCHAR(20)
        )
    """)

    conn.commit()
    cur.close()
    conn.close()


# Insert from CSV
def insert_from_csv(filename):
    conn = connect()
    cur = conn.cursor()

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                (row["name"], row["phone"])
            )

    conn.commit()
    cur.close()
    conn.close()


# Insert from console
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()


# Show all contacts
def show_contacts():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


# Search contacts
def search_contacts(keyword):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM phonebook WHERE name ILIKE %s OR phone LIKE %s",
        (f"%{keyword}%", f"{keyword}%")
    )

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


# Update contact
def update_contact(old_name):
    conn = connect()
    cur = conn.cursor()

    new_name = input("New name: ")
    new_phone = input("New phone: ")

    cur.execute(
        "UPDATE phonebook SET name=%s, phone=%s WHERE name=%s",
        (new_name, new_phone, old_name)
    )

    conn.commit()
    cur.close()
    conn.close()


# Delete contact
def delete_contact(value):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM phonebook WHERE name=%s OR phone=%s",
        (value, value)
    )

    conn.commit()
    cur.close()
    conn.close()


# Menu
def menu():
    create_table()

    while True:
        print("\nPHONEBOOK MENU")
        print("1. Import from CSV")
        print("2. Add contact")
        print("3. Show contacts")
        print("4. Search contact")
        print("5. Update contact")
        print("6. Delete contact")
        print("7. Exit")

        choice = input("Choose: ")

        if choice == "1":
            insert_from_csv("contacts.csv")

        elif choice == "2":
            insert_from_console()

        elif choice == "3":
            show_contacts()

        elif choice == "4":
            keyword = input("Search: ")
            search_contacts(keyword)

        elif choice == "5":
            old_name = input("Enter contact name to update: ")
            update_contact(old_name)

        elif choice == "6":
            value = input("Enter name or phone to delete: ")
            delete_contact(value)

        elif choice == "7":
            break

        else:
            print("Invalid choice")


menu()