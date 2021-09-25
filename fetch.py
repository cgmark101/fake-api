import requests

r = requests.get('http://localhost:8001/users')

r = r.json()

print(r)