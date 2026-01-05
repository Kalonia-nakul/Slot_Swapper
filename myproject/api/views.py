from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

endpoint = 'http://localhost:8000/'
    
def login_page(request):
    response = requests.get( f'{endpoint}api/login' )

    html_content = response.json().get('data')
    return HttpResponse(html_content)