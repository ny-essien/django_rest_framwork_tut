import requests

endpoint = "https://httpbin.org"
endpoint = "https://httpbin.org/anything"

endpoint = " http://127.0.0.1:8000/"

get_response = requests.get(endpoint, json = {"query" : "hello world"})
get_response = requests.get(endpoint, data = {'query' : "12345"})
get_response = requests.get(endpoint, json = {"query": "Hello world"})


print(get_response.text)

#print(get_response.json())