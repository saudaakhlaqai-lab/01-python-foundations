def show_client (client):
    print("Name:", client["name"])
    print("Age:", client["age"])
    print("Gender:", client["gender"])
clients =[
    
     {"name" : "Bobby",
      "age" : 35,
     "gender" : "male"
        },
    { 
     "name" : "Samantha",
      "age" : 28,
     "gender" : "female"
        },
    {
        "name": "Michael",
        "age":42,
        "gender": "male"
    }
]

def client_type(client):
    if client ["age"] < 18:
        return "Minor"
    else:
        return "Adult"
for client in clients:
    show_client(client)
    print ("Client Type:", client_type(client))
    print("------")
