from django.shortcuts import render
from django.http import JsonResponse
from .parser import user
from django.core import serializers

# Create your views here.

def statuses_lookup(request):
    api = TwitterAPI()
    response = api.statuses_lookup(['1331950835413053440'])
    user_object = user(response[0]._json['user'])    
    user_object.save()
    return JsonResponse(response[0]._json['user'])

