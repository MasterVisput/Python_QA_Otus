import requests

r = requests.get('https://software-testing.ru')
hed = r.headers


for k, v in hed.items():
    print(k, '==>', v)

