from django.contrib import admin
from django.urls import path
from home.views import *

urlpatterns = [
    path('', home, name="home"),
    path('contact/', contact, name="contact"),
    path('about/', about, name="about"),
    path('create-account/', create_account, name="create_account"),
    path('forgot-password/', forgot_password, name="forgot_password"),
    path('login/', login, name="login"),
    

    path('admin/', admin.site.urls),
]
