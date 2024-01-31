import requests

endpoint = "https://httpbin.org"
endpoint = "https://httpbin.org/anything"

endpoint = "http://127.0.0.1:8000/"
#endpoint = "http://localhost:8000/"
endpoint = "http://localhost:8000/api/?abc=123"

#get_response = requests.get(endpoint, json = {"query" : "hello world"})
#get_response = requests.get(endpoint, data = {'query' : "12345"})
#params arguments are just query parameters
get_response = requests.get(endpoint, params= {"abc":123}, json = {"query": "Hello world"})


print(get_response.text)

#to get the status code
print(get_response.status_code)

print(get_response.json())
#printing out the JSON message
#print(get_response.json()['message'])