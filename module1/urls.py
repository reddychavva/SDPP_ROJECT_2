"""
URL configuration for TTM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include

from .views import *


class Homepage:
    pass


urlpatterns = [
    path('cupid/', hello1),
    path('hello/',hello,name='hello'),
    path('',newhomepage,name='newhomepage'),
    path('travelpage/',travelpage,name='travelpage'),
    path('console/',print_to_console,name='print_to_console'),
    path('p/',print1,name='print1'),
    path('regicall/', registercall, name='registercall'),
    path('regilogin/', registerloginfunction, name="registerloginfunction"),
    path('ran/',random123,name='random123'),
#urls.py
    path('date_request/', getdate_req, name='getdate_req'),
    path('getdate/', getdate_template, name='getdate_template'),
    path('t/',Homepage,name = 'Homepage.html'),
    path('w/',weatherpagecall,name='weatherapi.html'),
    path('weather/',weatherlogic,name='weatherapi.html'),
    path('login/', login, name='login1'),
    path('register/', signup, name='signup2'),
    path('login1/',login1,name='login12'),
    path('signup1/',signup1,name='signup12'),
    path('logut1/',logout,name='logout12'),
    path('R/',regis, name='regis'),
    path('contactmail/',contactmail, name='contactmail')

]
