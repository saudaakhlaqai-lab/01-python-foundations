import csv

clients = []


def register_client():
    try:
        name = input("Client's Name: ")
        age = int(input("Client's Age: "))
        number = input("Client's Number: ")
        concern = input("Client's Concern: ")
        clients.append({
            "name": name,
            "age": age,
            "number": number,
            "concern": concern
        })
    except ValueError:
        print("\nAge must be in numbers only.\n")


# create a dictionary and add it to the clients list.
def show_clients():
    print("\nList of Clients:")
    if not clients:
        print("No clients registered.")
        return
    for client in clients:
        print("Name:", client["name"])
        print("Age:", client["age"])
        print("Number:", client["number"])
        print("Concern:", client["concern"])
        print()
    else:
        ("Client not found")


def search_client():
    search_name = input("Enter the name of the client to search: ")
    found = False
    for client in clients:
        if client["name"].lower() == search_name.lower():
            print("Client found:")
            print("Name:", client["name"])
            print("Age:", client["age"])
            print("Number:", client["number"])
            print("Concern:", client["concern"])
            print()
            found = True
            break
    if not found:
        print("Client not found.")


def save_csv():
    with open("clients.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "Number", "Concern"])
        for client in clients:
            writer.writerow([
                client["name"],
                client["age"],
                client["number"],
                client["concern"]
            ])
    print("Clients saved to clients.csv")


def update_client():
    search_name = input("Enter the name of the client to update: ")
    found = False
    for client in clients:
        if client["name"].lower() == search_name.lower():
            print("Client found. Enter new details:")
            client["name"] = input("Client's Name: ")
            client["age"] = int(input("Client's Age: "))
            client["number"] = input("Client's Number: ")
            client["concern"] = input("Enter new concern: ")
            print()
            found = True
            break
    if not found:
        print("Client not found!")


def delete_client():
    search_client = input("Enter client's name to be deleted: ")
    found = False
    for client in clients:
        if client["name"].lower() == search_client.lower():
            clients.remove(client)
            print("\nClient deleted successfully.")
            found = True
            break
    if not found:
        print("Client not found.")


while True:
    print("1. Register Client")
    print("2. Show Clients")
    print("3. Save CSV")
    print("4. Search Client")
    print("5. Update Client")
    print("6. Delete Client")
    print("7. Exit")
    choice = input("Choose from 1-7: ")

    if choice == "1":
        register_client()
    elif choice == "2":
        show_clients()
    elif choice == "3":
        save_csv()
    elif choice == "4":
        search_client()
    elif choice == "5":
        update_client()
    elif choice == "6":
        delete_client()
    elif choice == "7":
        print("Goodbye")
        break
    else:
        print("Invalid choice.")
    
    