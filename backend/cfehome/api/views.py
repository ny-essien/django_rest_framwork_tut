import json
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse

# Create your views here.
def api_home(request, *args, **kwargs):

    #request -> HttpRequest -> Django
    #print(dir(request))
    #request.body

    print(request.GET)

    body = request.body # byte string of JSON data

    #converting the data to a python dictionary
    try:
        data = json.loads(body) #takes a string of data and converts it into a python dictionary
    
    except:
        pass

    print(data)
    print(data.keys())
    #return JsonResponse({"message" : "Hi there, this is your Django API Response"})
    #creating a header
    #data['headers'] = request.headers
    print(request.headers)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)
