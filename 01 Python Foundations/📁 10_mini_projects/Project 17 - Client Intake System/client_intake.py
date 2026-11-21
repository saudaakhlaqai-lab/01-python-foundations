import csv

clients = []


def add_client():
    try:
        name = input("Enter client's name: ")
        age = int(input("Enter client's age: "))
        concern = input("Enter client's concern: ")
        client = {
            "Name": name,
            "Age": age,
            "Concern": concern,
        }
        clients.append(client)
        print("\nClient added successfully!\n")
    except ValueError:
        print("\nAge must be in numbers only.\n")


def show_clients():
    print("\n List of Clients:")
    for client in clients:
        print("Name:", client["Name"])
        print("Age:", client["Age"])
        print("Concern:", client["Concern"])
        print()


def save_csv():
    with open("client.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "Concern"])
        for client in clients:
            writer.writerow([
                client["Name"],
                client["Age"],
                client["Concern"]
                ])
    print("\nClient data saved to CSV file.\n")


add_client()
show_clients()
save_csv()