from django.shortcuts import render
import random

def home(request):
    
    return render(request, 'generator/home.html')

def about(request):
    
    return render(request, 'generator/about.html')

def password(request):
    generated_password = ''
    lenght = int(request.GET.get('length', 8)) # 8 = default value
    characters = list('abcdefghijklmnopqrstuvwxyz')
    uppercase = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    numbers = list('0123456789')
    special = list('!@#$%*')

    if request.GET.get('uppercase'):
        characters.extend(uppercase)
    if request.GET.get('numbers'):
        characters.extend(numbers)
    if request.GET.get('special'):
        characters.extend(special)

    for i in range(lenght):

        generated_password += random.choice(characters)


    return render(request, 'generator/password.html', { 'password': generated_password })