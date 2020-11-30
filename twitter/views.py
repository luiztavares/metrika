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

def get_status(request):
    api = TwitterAPI()

    response = api.get_status('1331996558754254851')
    tweet = status_parse(response._json) 
    
    return JsonResponse(response._json)

def get_user(request):
    api = TwitterAPI()

    response = api.get_user('45870897')
    user = user_parse(response._json) 
    
    return JsonResponse(response._json)

def get_friends(request):
    api = TwitterAPI()
    user_id = '45870897'

    for response in api.get_friends(user_id):
        follow_parse(source= user_id,target= response)
    
    return JsonResponse(response)

def get_followers(request):
    api = TwitterAPI()
    user_id = '45870897'
    
    for response in api.get_followers(user_id):
        follow_parse(source= response,target= user_id)
    
    return JsonResponse(response)

