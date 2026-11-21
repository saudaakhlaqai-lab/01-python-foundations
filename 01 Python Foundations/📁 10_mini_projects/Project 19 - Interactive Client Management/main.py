import csv

clients = []
def register_client():
    try:
        name = input("Client's Name:")
        age = int(input("Client's Age:"))
        number = input("Client's Number:")
        clients.append({
            "name": name,
            "age": age,
            "number": number
        })
    except ValueError:
        print("\n Age must be in numbers only.\n")
        
def show_clients():
    print("\n List of Clients:")
    for client in clients:
        print("Name:", client["name"])
        print("Age:", client["age"])
        print("Number:", client["number"])
    if len(clients) == 0:
            print("No clients registered yet.")
def save_csv():
    with open ("clients.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age","Number"])
        for client in clients:
            writer.writerow([
                client["name"],
                client["age"],
                client["number"]
            ])
def menu():
    while True:
        print("\n Client Management System")
        print("1.Register Client")
        print("2.Show Clients")
        print("3.Save to CSV")
        print("4.Exit")
        choice = input("Enter your choice(1-4):")
        if choice == "1":
            register_client()
        elif choice == "2":
            show_clients()
        elif choice == "3":
            save_csv()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
menu()