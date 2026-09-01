import requests

response = requests.get("https://reqres.in/api/users/2")

print("Status code:", response.status_code)
print("JSON body:", response.json())

data = response.json()
print("User's first name:", data["data"]["first_name"])
print("User's email:", data["data"]["email"])

payload = {"name": "morpheus", "job": "leader"}
response = requests.post("https://reqres.in/api/users", json=payload)

print("Status code:", response.status_code)
print("Created user:", response.json())

response = requests.get("https://reqres.in/api/users/9999")
print("Status code:", response.status_code)

if response.status_code == 404:
    print("Correctly received 404 for non-existent user")
