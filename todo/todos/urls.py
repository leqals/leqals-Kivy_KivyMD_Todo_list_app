from django.urls import path
from .views import *

urlpatterns = [
    
    path("", login_page, name='login_page'),
    path('/', home, name='home'),
    path("doLogin/", doLogin, name='user_login'),

]
