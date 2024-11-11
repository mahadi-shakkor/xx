from django.contrib import admin
from django.urls import path
from home.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home, name="home"),
    path('rp/', recipes, name="recipes"),
    path('contact/', contact, name="contact"),
    path('about/', about, name="about"),
    path('create-account/', create_account, name="create_account"),
    path('forgot-password/', forgot_password, name="forgot_password"),
    path('login/', login, name="login"),
    
    path('delete-recipe/<int:id>/', delete_recipe, name="delete_recipe"),

    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files during development
urlpatterns += staticfiles_urlpatterns()