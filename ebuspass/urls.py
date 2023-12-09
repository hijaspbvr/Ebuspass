"""ebuspass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from ebusapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('adminhome', views.adminhome, name='adminhome'),
    path('admindepo', views.admindepo, name='admindepo'),
    path('admindepodelete', views.admindepodelete, name='admindepodelete'),
    path('admincourse', views.admincourse, name='admincourse'),
    path('admincoursedelete', views.admincoursedelete, name='admincoursedelete'),
    path('admininstitute', views.admininstitute, name='admininstitute'),
    path('admininstitutedelete', views.admininstitutedelete, name='admininstitutedelete'),
    path('admincardtype', views.admincardtype, name='admincardtype'),
    path('admincarddelete', views.admincarddelete, name='admincarddelete'),
    path('adminstop', views.adminstop, name='adminstop'),
    path('adminstopdelete', views.adminstopdelete, name='adminstopdelete'),
    path('adminrate', views.adminrate, name='adminrate'),
    path('adminratedelete', views.adminratedelete, name='adminratedelete'),
    path('depohome', views.depohome, name='depohome'),
    path('depoapplications', views.depoapplications, name='depoapplications'),
    path('depopayments', views.depopayments, name='depopayments'),
    path('depochangepassword', views.depochangepassword, name='depochangepassword'),
    path('institutehome', views.institutehome, name='institutehome'),
    path('institutecourse', views.institutecourse, name='institutecourse'),
    path('instituteaffiliation', views.instituteaffiliation, name='instituteaffiliation'),
    path('institutestudents', views.institutestudents, name='institutestudents'),
    path('institutestudentapprove', views.institutestudentapprove, name='institutestudentapprove'),
    path('institutestudentreject', views.institutestudentreject, name='institutestudentreject'),
    path('studenthome', views.studenthome, name='studenthome'),
    path('studentdetails', views.studentdetails, name='studentdetails'),
    path('studentpayment', views.studentpayment, name='studentpayment'),
    path('studentreg', views.studentreg, name='studentreg'),
    path('institutereg', views.institutereg, name='institutereg'),
    path('payment', views.payment, name='payment'),
    path('depoapplicationapprove', views.depoapplicationapprove, name='depoapplicationapprove'),
    path('studentcardgenerator', views.studentcardgenerator, name='studentcardgenerator'),
    path('studentgeneratecard',views.studentgeneratecard,name="studentcardgenerator")
]

