from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	response = HttpResponse("Home")
	return response

def write(request):
	return HttpResponse("Write")