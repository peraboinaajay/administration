from django.shortcuts import render
from admissions.models import School


# Create your views here.
#fuction based views
def homepage(request):
    return render(request,"index.html")

def addadmission(request):
    ajay=School.objects.all();
    student={'allstudents':ajay}
    return render(request,'admissions/admission-reports.html',student);

 



def admissionreport(request):
    
    return render(request,'admissions/new-admission.html',);

