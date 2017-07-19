from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Room
#http://localhost:8000/access_room/?temp=25.0&humi=80.0
def access_room(request):
	if request.method == 'GET':
		#print "GET: %s"%request.GET
		_temp=float(request.GET.get("temp",None))
		_humi=float(request.GET.get("humi",None))
		
		print "temperature: %s"%_temp
		print "humidity: %s"%_humi

		Room.objects.create(temp=_temp, humi=_humi)
	else:
		print "Not GET method"
	return HttpResponse("Hello")