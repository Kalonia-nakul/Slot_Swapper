from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user_slot_data/<str:user>/', views.user_slot_data, name='user_slot_data'),
    path('slot_data/<str:user>/', views.slot_data, name='slot_data'),
    path('add_slot/' , views.add_slot , name = 'add_slot'),
    path('register/' , views.register_user , name = 'register_user'),
    path('delete_slot/<int:slot_id>/' , views.delete_slot , name = 'delete_slot'),
    path('request_swap/' , views.request_swap , name = 'request_swap'),
]