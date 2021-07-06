import requests

app = requests.get("http://localhost:8000/api/employees/")
employee = app.json()
print(employee[0].get('birthday'))