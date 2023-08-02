from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
#fuction based views

def addadmission(request):
    return HttpResponse("<h1>this is the admission view<h1/><h2>Welcome to my school app<h2/>")
 



def admissionreport(request):
    return HttpResponse("this the admissions report view") 
