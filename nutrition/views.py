from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
#action

def say_hello(request):
    #return HttpResponse('COST EFFICIENT BALANCED DIET')
    template = loader.get_template('hello.html')
    return HttpResponse(template.render())

def submit_request(request):
    # return HttpResponse('COST EFFICIENT BALANCED DIET')
    template= loader.get_template('base.html')
    return HttpResponse(template.render())
   
