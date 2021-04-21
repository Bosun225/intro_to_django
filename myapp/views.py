from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Congratulations Abdulqudus, Yayyyy ... you have created your first app")