from django.shortcuts import render
from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Hey I am a Django Server.")
def success_page(request):
    return HttpResponse("<h1>Hey this is a Success page</h1>")


def home(request):
    return render(request, "home/index.html")
