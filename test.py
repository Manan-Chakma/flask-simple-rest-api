import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + 'product')
print(response.json())
response = requests.get(BASE + 'product/1')
print(response.json())

response = requests.put(BASE + 'product')
print(response.json())
response = requests.put(BASE + 'product/1')
print(response.json())

response = requests.delete(BASE + 'product')
print(response.json())
response = requests.delete(BASE + 'product/1')
print(response.json())

response = requests.post(BASE + 'product', {"product_name": 'Handi Biriyani'})
print(response.json())

response = requests.post(BASE + 'product')
print(response.json())