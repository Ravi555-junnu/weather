from django.shortcuts import render,redirect
from django.http import HttpResponse
import json 
import urllib.request

# Create your views here.

def index(request):
    if request.method=='POST':
        city=request.POST['city']
        res=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=2340d9849830b61491e974c545c67c23').read()
        json_data=json.loads(res)
        data={
            'country_code':str(json_data['sys']['country']),
            'coordinates': str(json_data['coord']['lon'])+" "+str(json_data['coord']['lat']),
            'temp' : str(json_data['main']['temp'])+'K',
            'pressure':str(json_data['main']['pressure']),
            'humidity':str(json_data['main']['humidity']),
            'city':city,
        }
    else:
        data={}
    return render(request,'index.html',data)