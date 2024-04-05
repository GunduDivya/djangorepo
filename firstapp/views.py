from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

# Create your views here.
class helloworld_view(View):
    def get(self,request):
        return HttpResponse('<h1>the response is from class bASED view</h1>')
