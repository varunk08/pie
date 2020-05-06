import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

print(type(res))
print(res.text[:250])