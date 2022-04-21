"""loginsys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
     path('',views.firstpage),
    path('first',views.firstpage,name="first"),
    #path('index',views.indexpage,name="index"),
    path('registration',views.userreg,name="reg"),
    path('login',views.loginpage,name="loginpage"),
    path('logout',views.logout,name="logout"),
    #path('index1',views.indexpage1,name="index1"),
    path('registration1',views.userreg1,name="reg1"),
    path('login1',views.loginpage1,name="loginpage1"),
    path('logout1',views.logout1,name="logout1"),
    path('meetdet1',views.meetdet1,name="meetdet1"),
    path('meettable1',views.showresults1,name="meettable1"),
    path('meettable',views.showresults,name="meettable"),
    #path('meettable2',views.showresults2,name="meettable2"),
    path('meetregister',views.usermeetreg,name="meetregister"),
    path('addparticipant1',views.usermeetreg1,name="addparticipant1"),
    path('viw1',views.viw,name='viw1'),
    path('viewmember1',views.viewmem,name="viewmember1"),
    path('aboutus',views.aboutus,name="aboutus"),
    path('contactus',views.contactus,name="contactus"),
    path('attendance',views.tablesjoin,name="attendance"),
    path('profile',views.profile,name='profile'),
]
