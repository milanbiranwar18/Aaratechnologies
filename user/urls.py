from django.urls import path
from . import views


urlpatterns = [
    path('user_registration/', views.Registration.as_view(), name='registration'),
    path('user_login/', views.Login.as_view(), name='login'),
    path('user_logout/', views.Logout.as_view(), name='user_logout'),
    path('dj-rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('dj-rest-auth/facebook/', FacebookLogin.as_view(), name='facebook_login'),

]
