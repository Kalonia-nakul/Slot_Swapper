from django.shortcuts import redirect, render
from django.http import HttpResponse
import requests

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



def signup_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        data = {
            'username': username,
            'email': email,
            'password': password
        }
        response = requests.post(f'{endpoint}register/', json=data)
        return redirect('login_page')
    return render(request, 'signup.html')


def home_page(request):
    if request.method == 'GET':
        global payload
        response = requests.get(f'{endpoint}user_slot_data/{payload["username"]}/', headers={'Authorization': f'Bearer {payload["access_token"]}'} ) 
        user_slots = response.json()
        response = requests.get(f'{endpoint}slot_data/{payload["username"]}/', headers={'Authorization': f'Bearer {payload["access_token"]}' })
        slots = response.json()
        return render(request, 'home.html', {'slots': slots , 'user_slots': user_slots , 'username': payload['username']})
     
    elif request.method == 'POST' :
        if request.POST.get('action') == 'delete':
            slot_id = request.POST.get('slot_id')
            response = requests.post(f'{endpoint}delete_slot/{slot_id}/', headers={'Authorization': f'Bearer {payload["access_token"]}'})
            return redirect('home_page')

        else : 
            topic = request.POST.get('topic')
            Date = request.POST.get('Date')
            starttime = request.POST.get('starttime')
            endtime = request.POST.get('endtime')
            status = request.POST.get('status')
            
            data = {
                'user' : payload['username'],
                'topic': topic,
                'Date': Date,
                'starttime': starttime,
                'endtime': endtime,
                'status': status
            }
            response = requests.post(f'{endpoint}add_slot/', json=data , headers={'Authorization': f'Bearer {payload["access_token"]}'})
            return redirect('home_page')
        

def request_swap(request , slot_id):

    if request.method == 'GET' :
        slot_id = request.GET.get('slot_id')
        username = request.GET.get('username')
        response = requests.get(f'{endpoint}user_slot_data/{username}/', headers={'Authorization': f'Bearer {payload["access_token"]}'} ) 
        user_slots = response.json()
        return render(request, 'swap.html' , {'slot_id' : slot_id , 'username' : username , 'user_slots' : user_slots}) 
    
    elif request.method == 'POST' :
        swap_slot_id = request.POST.get('swap_slot_id')
        slot_id = request.POST.get('slot_id')
        username = request.POST.get('username')
        response = requests