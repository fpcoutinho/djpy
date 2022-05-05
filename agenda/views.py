from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'accounts/templates/login.html')
