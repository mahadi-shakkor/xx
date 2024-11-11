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
