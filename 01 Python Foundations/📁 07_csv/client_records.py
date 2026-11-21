import csv
clients=[
    ["name", "age", "concern"],
    ["Sam", 23, "anxiety"],
    ["Alice", 43, "depression"],
    ["John", 35, "stress management"]
]
with open("client.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(clients)
    print("Client records saved successfully in client.csv")
    