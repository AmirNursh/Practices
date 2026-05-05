from connect import connect


# Search by pattern
def search_contacts(pattern):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_pattern(%s)", (pattern,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


# Upsert contact
def upsert_contact():
    name = input("Name: ")
    phone = input("Phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))

    conn.commit()
    cur.close()
    conn.close()


# Insert many users
def insert_many():
    names = ["Ali", "Amir", "Aruzhan"]
    phones = ["87012345678", "87098765432", "123"]

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "CALL insert_many_users(%s, %s)",
        (names, phones)
    )

    conn.commit()
    cur.close()
    conn.close()


# Pagination
def show_paginated(limit, offset):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM get_contacts_paginated(%s, %s)",
        (limit, offset)
    )

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


# Delete
def delete_contact():
    value = input("Enter name or phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL delete_contact(%s)", (value,))

    conn.commit()
    cur.close()
    conn.close()


# Menu
while True:
    print("\nPHONEBOOK")
    print("1. Search")
    print("2. Upsert")
    print("3. Insert many")
    print("4. Pagination")
    print("5. Delete")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        pattern = input("Pattern: ")
        search_contacts(pattern)

    elif choice == "2":
        upsert_contact()

    elif choice == "3":
        insert_many()

    elif choice == "4":
        limit = int(input("Limit: "))
        offset = int(input("Offset: "))
        show_paginated(limit, offset)

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        break