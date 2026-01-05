from django.urls import path
from . import views 

urlpatterns = [ 
    path('login/', views.login_page, name='login_page'),
    path('home/' , views.home_page , name = 'home_page'),
]