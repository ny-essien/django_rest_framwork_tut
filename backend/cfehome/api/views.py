import json
from django.forms.models import model_to_dict
from products.models import Products
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse

# Create your views here.
def api_home(request, *args, **kwargs):

    model_data = Products.objects.all().order_by("?").first()
    data = {}

    if model_data:

        data = model_to_dict(model_data, fields= ['id','title','price'])
        #convertiing dict str to json str
        #json_data_str = json.dumps(data)
        #data['id'] = model_data.id
        #data['title'] = model_data.title
        #data['context'] = model_data.content
        #data['price'] = model_data.price

        #model instance (model_data)
        #turn a python dict
        #return JSON to client
    #return HttpResponse(data, headers = {"content_type": "application/json"})
    #return HttpResponse(json_data_str, headers = {"content-type" : "application/json"})    

    return JsonResponse(data)
     

