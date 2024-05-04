from django.urls import path
from . import views


urlpatterns = [
    path('user_registration/', views.Registration.as_view(), name='registration'),
    path('user_login/', views.Login.as_view(), name='login'),
    path('user_logout/', views.Logout.as_view(), name='user_logout'),
]
