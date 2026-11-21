import csv 
import json
clients = []
def register_client():
    try:
        name = input("Client's Name:")
        age = int(input("Client's Age:"))
        concern = input("Concern:")
        email = input("Email:")
        client = {
            "Name": name,
            "Age": age,
            "Concern": concern,
            "Email": email
        }
        clients.append(client)
        print("\n Client Registered Successfully!\n")
    except ValueError:
        print("\n Age must be in numbers only.\n")
def show_clients():
    print("\n List of Clients:")
    for client in clients:
        print("Name:", client["Name"])
        print("Age:", client["Age"])
        print("Concern:", client["Concern"])
        print("Email:", client["Email"])
        if client["Age"]<18:
            print("Note: Client is minor")
        else:
            print("Client is an adult")
print("-" * 40)
print("Total Client's :", len(clients))
def save_csv():

    with open("clients.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["Name", "Age", "Concern", "Email"])

        for client in clients:

            writer.writerow([

                client["name"],

                client["age"],

                client["concern"],

                client["email"]

            ])

    print("\nCSV Saved Successfully!\n")
def json_save():
    print("\n ===============JSON===============\n")
    print(json.dumps (clients, indent=4))
register_client()
register_client()
print(clients)
save_csv()
json_save()