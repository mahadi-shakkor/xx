from django.shortcuts import render
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
