from django.shortcuts import render



# Create your views here.
#fuction based views

def addadmission(request):
    return render(request,'admissions/new-admission.html')

 



def admissionreport(request):
    value={"name":"all","mail":"ajay@mail"}
    return render(request,'admissions/admission-reports.html',value)

