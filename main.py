import requests
import pprint

print('ДЗ. Задача 1.')

params1 = {
    'q': 'language:html'
}

response = requests.get('https://api.github.com/search/repositories', params=params1)
print(response.status_code)
response_json = response.json()
pprint.pprint(response_json)


print('ДЗ. Задача 2.')

params2 = {
    'userId': 1
}

response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params2)
print(response.status_code)
response_json = response.json()
#pprint.pprint(response_json)

for i in response_json:
    print(i)


print('ДЗ. Задача 3.')

data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

response = requests.post('https://jsonplaceholder.typicode.com/posts', data=data)
print(response.status_code)
response_json = response.json()
print(response_json)


