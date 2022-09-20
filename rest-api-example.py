import requests

response = requests.get('http://127.0.0.1:8000/apiv0/books/?page=2')
print(response.text)