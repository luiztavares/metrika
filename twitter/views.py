from django.shortcuts import render
from django.http import JsonResponse
from .parser import *
from django.core import serializers
from .api import TwitterAPI

# Create your views here.

def statuses_lookup(request):
    api = TwitterAPI()

    response = api.statuses_lookup(['1331950835413053440','1332338713746083843','1331996558754254851'])
    for status in response:
        status_parse(status._json)    
    
    return JsonResponse(response[-1]._json)

def user_timeline(request):
    api = TwitterAPI()

    response = api.user_timeline('midianinja')
    for status in response:
        status_parse(status._json) 
    
    return JsonResponse(response[-1]._json)
