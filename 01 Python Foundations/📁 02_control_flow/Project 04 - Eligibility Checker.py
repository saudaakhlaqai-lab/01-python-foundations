print("====Eligibility calculator===")
age = float(input("Enter your age:"))
if age>=18:
    print("You're eligible.")
else:
    print("You're not eligible.")
    
### Real World Project on Counselling Consent Form
age = int(input("Enter your age:"))

if age<18:
    print("Parents and Guardian consent required.")
else:
    print("You re eligible.")