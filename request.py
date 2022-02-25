import requests

r = requests.post('https://httpbin.org/post', data={'key':'ass'})

print(r)
