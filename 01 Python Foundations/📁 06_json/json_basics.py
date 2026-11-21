import json
client_data = {
    "name": "John Doe",
    "age": 35,
    "gender": "male",
    "concern":"Anxiety attacks"
}
json_data = json.dumps(client_data, indent=4)
print(json_data)

python_data = json.loads(json_data)
print("client's name:", python_data["name"])