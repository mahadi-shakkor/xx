from django.shortcuts import render,redirect
from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Hey I am a Django Server.")
def success_page(request):
    return HttpResponse("<h1>Hey this is a Success page</h1>")


def home(request):

    peoples = [
    {'name': 'Abhijeet Gupta', 'age': 26},
    {'name': 'Rohan Sharma', 'age': 23},
    {'name': 'Vicky Kaushal', 'age': 17},
    {'name': 'Deepanshu Chaurasiya', 'age': 16},
    {'name': 'Sandeep', 'age': 63}
    ]   



    return render(request, "home/index.html", context={'peoples':peoples})

def about(request):
    return render(request, "home/about.html")

def contact(request):
    return render(request, "home/contact.html")

def login(request):
    return render(request, "home/login.html")

def create_account(request):
    return render(request, "home/create-account.html")

def forgot_password(request):
    return render(request, "home/forgot-password.html")
# from django.shortcuts import render
from .models import *

def recipes(request):
    if request.method == "POST":
        data = request.POST
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')

        Recipe.objects.create(
            recipe_name=recipe_name,  # match the field name here
            recipe_description=recipe_description,  # match the field name here
            recipe_image=recipe_image  # match the field name here
        )
        return redirect('/rp/')
    
    queryset = Recipe.objects.all()
    context = {'recipes': queryset}
 

    return render(request, 'home/receipes.html', context)

def delete_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/rp/')
