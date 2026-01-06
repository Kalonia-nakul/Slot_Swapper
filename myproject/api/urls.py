from django.urls import path
from . import views 

urlpatterns = [ 
    path('login/', views.login_page, name='login_page'),
    path('signup/', views.signup_page, name='signup_page'),
    path('home/' , views.home_page , name = 'home_page'),
    path('swap/<int:slot_id>/' , views.request_swap , name = 'request_swap'),
]