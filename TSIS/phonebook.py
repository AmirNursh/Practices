import json
import csv
from connect import connect


def add_contact():
    conn = connect()
    cur = conn.cursor()

    name = input("Name: ")
    email = input("Email: ")
    birthday = input("Birthday (YYYY-MM-DD): ")
    group_name = input("Group: ")
    phone = input("Phone: ")
    phone_type = input("Type (home/work/mobile): ")

    cur.execute(
        "INSERT INTO groups(name) VALUES(%s) ON CONFLICT(name) DO NOTHING",
        (group_name,)
    )

    cur.execute("SELECT id FROM groups WHERE name=%s", (group_name,))
    group_id = cur.fetchone()[0]

    cur.execute("""
        INSERT INTO contacts(name,email,birthday,group_id)
        VALUES(%s,%s,%s,%s)
    """, (name, email, birthday, group_id))

    cur.execute("SELECT id FROM contacts WHERE name=%s", (name,))
    contact_id = cur.fetchone()[0]

    cur.execute("""
        INSERT INTO phones(contact_id,phone,type)
        VALUES(%s,%s,%s)
    """, (contact_id, phone, phone_type))

    conn.commit()
    cur.close()
    conn.close()


def filter_by_group():
    group = input("Group: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.name, c.email
        FROM contacts c
        JOIN groups g ON c.group_id=g.id
        WHERE g.name=%s
    """, (group,))

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()


def search_email():
    email = input("Email part: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT name,email
        FROM contacts
        WHERE email ILIKE %s
    """, ('%' + email + '%',))

    print(cur.fetchall())

    cur.close()
    conn.close()


def sort_contacts():
    field = input("Sort by (name/birthday/date): ")

    mapping = {
        "name": "name",
        "birthday": "birthday",
        "date": "created_at"
    }

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        f"SELECT * FROM contacts ORDER BY {mapping[field]}"
    )

    print(cur.fetchall())

    cur.close()
    conn.close()


def export_json():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.name,c.email,c.birthday,g.name,p.phone,p.type
        FROM contacts c
        LEFT JOIN groups g ON c.group_id=g.id
        LEFT JOIN phones p ON c.id=p.contact_id
    """)

    data = cur.fetchall()

    contacts = []

    for row in data:
        contacts.append({
            "name": row[0],
            "email": row[1],
            "birthday": str(row[2]),
            "group": row[3],
            "phone": row[4],
            "type": row[5]
        })

    with open("contacts.json", "w") as f:
        json.dump(contacts, f, indent=4)

    cur.close()
    conn.close()


def import_json():
    with open("contacts.json", "r") as f:
        contacts = json.load(f)

    conn = connect()
    cur = conn.cursor()

    for contact in contacts:
        cur.execute(
            "SELECT * FROM contacts WHERE name=%s",
            (contact["name"],)
        )

        if cur.fetchone():
            action = input(
                f"{contact['name']} exists. skip/overwrite: "
            )

            if action == "skip":
                continue

            if action == "overwrite":
                cur.execute(
                    "DELETE FROM contacts WHERE name=%s",
                    (contact["name"],)
                )

        cur.execute(
            "INSERT INTO groups(name) VALUES(%s) ON CONFLICT(name) DO NOTHING",
            (contact["group"],)
        )

        cur.execute(
            "SELECT id FROM groups WHERE name=%s",
            (contact["group"],)
        )

        group_id = cur.fetchone()[0]

        cur.execute("""
            INSERT INTO contacts(name,email,birthday,group_id)
            VALUES(%s,%s,%s,%s)
        """, (
            contact["name"],
            contact["email"],
            contact["birthday"],
            group_id
        ))

    conn.commit()
    cur.close()
    conn.close()


def menu():
    while True:
        print("1 Add")
        print("2 Filter by group")
        print("3 Search by email")
        print("4 Sort")
        print("5 Export JSON")
        print("6 Import JSON")
        print("0 Exit")

        choice = input()

        if choice == "1":
            add_contact()
        elif choice == "2":
            filter_by_group()
        elif choice == "3":
            search_email()
        elif choice == "4":
            sort_contacts()
        elif choice == "5":
            export_json()
        elif choice == "6":
            import_json()
        elif choice == "0":
            break


menu()
