from django.shortcuts import render
from django.http import HttpResponse 
import random

# Create your views here.
def home(request):
    return render(request,'app/home.html')

def password(request):
    charachters= list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        charachters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('numbers'):
        charachters.extend(list('0123456789'))

    if request.GET.get('special'):
        charachters.extend(list('!@#$%^&*()'))
    
    length=int(request.GET.get('length',12))
    password=''
    for x in range(length):
        password += random.choice(charachters)

    return render(request,'app/password.html',{'password': password})

def about_me(request):
    return render(request,'app/aboutme.html')