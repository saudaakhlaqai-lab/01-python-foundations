import csv

def save_csv(clients):
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
def load_csv():

    clients = []

    clients.append("Aisha")

    return clients