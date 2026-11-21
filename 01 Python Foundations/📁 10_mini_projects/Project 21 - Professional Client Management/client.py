
def register_client(clients):
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
def show_clients(clients):
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


def search_client(clients):
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
def update_client(clients):
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


def delete_client(clients):
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
