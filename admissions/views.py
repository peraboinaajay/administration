from django.shortcuts import render
from admissions.models import School
from admissions.forms import studentmodelform
from admissions.forms import vendorform


# Create your views here.
#fuction based views
def homepage(request):
    return render(request,"index.html")

def addadmission(request):
    ajay=School.objects.all();
    student={'allstudents':ajay}

    return render(request,'admissions/admission-reports.html',student);

 



def admissionreport(request):
    form=studentmodelform
    studentform ={'form1':form}
    if request.method=='POST':
        form=studentmodelform(request.POST)
    

        if form.is_valid():
            form.save()
        return homepage(request)
    return render(request,'admissions/new-admission.html',studentform);
    
def addvendor(request):
    form =vendorform
    vform ={'form1':form}
    if request.method=='POST':
        form=studentmodelform(request.POST)
        if form.is_valid():
            print (form.cleaned_data['name'])
            print (form.cleaned_data['address'])
            print (form.cleaned_data['contact'])
            print (form.cleaned_data['item'])
        return homepage(request)
    return render(request,'admissions/add-vendor.html',vform);
    

