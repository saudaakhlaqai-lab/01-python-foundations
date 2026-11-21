try:

    name = input("Client Name: ")

    age = int(input("Age: "))

    print()

    print("Client Registered")

    print("Name:", name)

    print("Age:", age)

except ValueError:

    print()

    print("Please enter a valid age.")





#Challenge 1 This program takes two numbers as input from the user and calculates their sum. It also checks if the user has entered valid numbers.
    
try:
    first_number = int(input("Please enter the first number:"))
    second_number = int(input("Please enter the second number:"))
    sum_result = int(input("Please enter the sum of two numbers:"))
except ValueError:
    print("Invalid input. Please enter valid numbers.")
    
#Challenge 2 This program takes a file name as input from the user and reads the contents of the file. It also checks if the file exists.

try:
    file_name = input("Please enter the file name:")
    file = open(file_name, "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File not found. Please check the file name and try again.")
    
#mini challenge 
try:
   client ={
       "Name:" : input("Enter client's name:"),
       "Age:" : int(input("Enter client's age:")),
       "City:" : input("Enter client's city:")
       } 
except ValueError:
    print("Enter age in numbers only")