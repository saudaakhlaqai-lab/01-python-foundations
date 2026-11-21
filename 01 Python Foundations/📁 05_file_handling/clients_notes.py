name = input("Enter client name: ")

file = open("notes.txt", "w")

file.write(name)

file.close()

print("Client saved successfully!")