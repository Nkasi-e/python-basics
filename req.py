import requests
import django

print(django.get_version())

url = 'https://jsonplaceholder.typicode.com/posts'

response = requests.get(url)
print(response.json())

if response.status_code == 200:
    print('success')
else:
    print('request failed')