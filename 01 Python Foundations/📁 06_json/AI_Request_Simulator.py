import json

client = {
    "name": "Aisha",
    "concern": "I overthink everything."
}

print("Sending to AI...")

request = json.dumps(client, indent=4)

print(request)

print()

print("AI Response")

response = {
    "summary": "Client reports excessive worrying."
}

print(json.dumps(response, indent=4))