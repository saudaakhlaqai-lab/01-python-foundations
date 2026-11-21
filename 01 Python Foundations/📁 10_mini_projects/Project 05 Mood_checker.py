mood = input("How are you feeling today?").lower()
if mood=="happy":
    print("Keep shining.")
elif mood=="sad":
    print("Dont lose hope")
elif mood=="stressed":
    print("Do some breathing excercise.")
else:
    print("Thank You for sharing how you feel.")
    
## Ticket Priority Routing Program
#AI Support Ticket Priority

priority= input("Enter ticket priority: ").lower()

if priority== "high":
    print("Notify the support manager immediately.")
elif priority== "medium":
    print("Notify to the support team")
elif priority == "low":
    print("Add to normal work routine")
else: 
    print("PRIORITY INVALID.")