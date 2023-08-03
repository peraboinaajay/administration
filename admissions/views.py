from django.shortcuts import render



# Create your views here.
#fuction based views
def homepage(request):
    return render(request,"index.html")

def addadmission(request):
    return render(request,'admissions/new-admission.html')

 



def admissionreport(request):
    value={"name":"all","mail":"ajay@mail"}
    return render(request,'admissions/admission-reports.html',value)

