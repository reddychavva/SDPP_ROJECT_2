import string
from random import random

from django.http import HttpResponse
from django.shortcuts import render

from . forms import *


# Create your views here.
def hello(request):
    return render(request, 'hello123.html')


def hello1(request):
    return HttpResponse("<center style=color:blue> Welcome to TTM Homepage</center>")


def newhomepage(request):
    return render(request, 'newhomepage.html')


def travelpage(request):
    return render(request, 'travelpage.html')


def print1(request):
    return render(request, 'print_to_console.html')


def print_to_console(request):
    global user_input
    if request.method == "POST":
        user_input = request.POST['tharun']
        print(f'user input :{user_input}')
    # return HttpResponse('Form submitted sucessfully')
    a1 = {'user_input': user_input}
    return render(request, 'print_to_console.html', a1)

def registercall(request):
    return render(request, 'register.html')


from .models import *
from django.shortcuts import render, redirect


def registerloginfunction(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phonenumber = request.POST.get('phonenumber')
        # check if email already exists
        if Register.objects.filter(email=email).exists():
            message1 = "Email already exists choose a different email"
            # return HttpsResponse("email already registered choose a different email")
            return render(request, 'register.html', {'message1': message1})
        # create a new Register instance and save it
        Register.objects.create(name=name, email=email, password=password, phonenumber=phonenumber)
        return redirect('Homepage')
    return render(request, 'register.html')


def rando(request):
    return render(request, 'random123.html')


import random, string


def random123(request):
    if request.method == "POST":
        in1 = request.POST['otp']
        in2 = int(in1)
        result = ''.join(random.sample(string.digits, in2))
        print(f'result:{result}')
        b = {'result': result}
    return render(request, "random123.html", b)


def getdate1(request):
    return render(request, 'getdate_template.html')


import datetime
from django.shortcuts import render


# views.py
def getdate_req(request):
    return render(request, 'getdate_template.html')
def hello(request):
    return render(request, 'Homepage.html')


def getdate_template(request):
    if request.method == 'POST':
        form = IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value = form.cleaned_data['integer_value']
            date_value = form.cleaned_data['date_value']
            updated_date = date_value + datetime.timedelta(days=integer_value)
            return render(request, 'getdate_template.html', {'updated_date': updated_date})
    else:
        form = IntegerDateForm()

    return render(request, 'getdate_template.html', {'form': form})

import requests

def weatherpagecall(request):
    return render(request,'weatherapi.html')

def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = 'fa544b9188184f5baabf4ad713065adb'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1= round(temperature - 273.15,2)
            return render(request, 'weatherappinput.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weatherappinput.html', {'error_message': error_message})

def signup(request):
     return render(request, 'signup.html')

def login(request):
     return render(request, 'login.html')

def login1(request):
            if request.method == 'POST':
                username = request.POST['username']
                pass1 = request.POST['password']
                user = auth.authenticate(username=username, password=pass1)
                if user is not None:
                    auth.login(request, user)
                    return render(request, 'Homepage.html')
                else:
                    messages.info(request, 'Invalid credentials')
                    return render(request, 'login.html')
            else:
                return render(request, 'login.html')

def signup1(request):
            if request.method == "POST":
                username = request.POST['username']
                pass1 = request.POST['password']
                pass2 = request.POST['password1']
                if pass1 == pass2:
                    if User.objects.filter(username=username).exists():
                        messages.info(request, 'OOPS! user name is alrady exist')
                        return render(request, 'signup.html')
                    else:
                        user = User.objects.create_user(username=username, password=pass1)
                        user.save()
                        messages.info(request, 'Account created successfully!!')
                        return render(request, 'login.html')
                else:

                    messages.info(request, 'password do not match')
                    return render(request, 'signup.html')

def logout(request):
            auth.logout(request)
            return render(request, 'newhomepage.html')




def regis(request):
    return render(request,"registerpage2.html")

def contactmail(request):
        if request.method == 'POST':
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            email = request.POST['email']
            comment = request.POST['comment']
            tosend = comment + '-----------------------------------This is just comment'
            data = contactus(firstname=firstname, lastname=lastname, email=email, comment=comment)
            data.save()
            return HttpResponse("<h1><center>Thank you for giving feedback </center></h1>")
            # send_mail(
            #     "Thank you for contacting Aditya's Travel Tourism and  Management",
            #     tosend, 'TPM.customercare@gmail.com', [email], fail_silently=False,
            # )
            # return HttpResponse('<h1><center>Mail sent successfully</center></h1>')
