from django.shortcuts import redirect, render
from django.http import HttpResponse
import requests
from swapper.models import CustomUser, Slots

# Create your views here.

endpoint = 'http://localhost:8000/api/'
payload = {}
    
def login_page(request):
    if request.method == 'POST':
        global payload 
        payload['username'] = request.POST.get('username')
        password = request.POST.get('password')
        
        data = {
            'username': payload['username'],
            'password': password
        }
        response = requests.post(f'{endpoint}token/', json=data)
        payload['access_token'] = response.json()['access']
        return redirect('home_page')
    return render(request, 'login.html')




def home_page(request):
    if request.method == 'GET':
        global payload
        response = requests.get(f'{endpoint}slot_data/', headers={'Authorization': f'Bearer {payload["access_token"]}'})
        slots = response.json()
        return render(request, 'home.html', {'slots': slots})
    
    elif request.method == 'POST' :
        topic = request.POST.get('topic')
        Date = request.POST.get('Date')
        starttime = request.POST.get('starttime')
        endtime = request.POST.get('endtime')
        status = request.POST.get('status')

        data = {
            'user' :  payload['username'],
            'topic': topic,
            'Date': Date,
            'starttime': starttime,
            'endtime': endtime,
            'status': status
        }
        print(data)

        response = requests.post(f'{endpoint}add_slot/', json=data, headers={'Authorization': f'Bearer {payload["access_token"]}'})
        
        return redirect('home_page')