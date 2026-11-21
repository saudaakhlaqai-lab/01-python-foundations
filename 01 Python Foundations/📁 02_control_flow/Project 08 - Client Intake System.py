def welcome():
    print("===================================")
    print("Client  Intake System")
    print("===================================")
welcome()
name = input("Enter client's name: ")
age = int(input("Enter client's age: "))
gender = input("Enter client's gender:")
reason = input("Enter reason for seeking services:")
print("=======Clients Information=======")
print("Client's Name:", name)
print("Client's Age:", age)
print("Client's Gender:", gender)
print("Reason for seeking services:", reason)
if age <13:
    print("Refer to child counseller.")
elif age<18:
    print("Refer to Adolescent Counseller.")
else:
    print("Adult Counseller will be assigned to you")
first_session = input("Is this your first session?(yes/no):").lower()
if first_session == "yes":
    print("Welcome to our services, we are glad you are here.We will guide you to our services.")
else:
    print("Welcome back, we are happy to see you again.")  
