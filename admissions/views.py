from django.shortcuts import render
from admissions.models import School
from admissions.models import teacher
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView
from admissions.forms import studentmodelform
from admissions.forms import vendorform
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required,permission_required


# Create your views here.
#fuction based views
@login_required
def homepage(request):
    return render(request,"index.html")

def logouted(request):
    return render(request,"logout.html")

@login_required
@permission_required('admissions.view_school')
def addadmission(request):
    ajay=School.objects.all();
    student={'allstudents':ajay}

    return render(request,'admissions/admission-reports.html',student);

 


@login_required
def admissionreport(request):
    form=studentmodelform
    studentform ={'form1':form}
    if request.method=='POST':
        form=studentmodelform(request.POST)
    

        if form.is_valid():
            form.save()
        return homepage(request)
    return render(request,'admissions/new-admission.html',studentform);
@login_required    
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
@login_required    
def updatestudent(request,id):
    s=School.objects.get(id=id)
    form=studentmodelform(instance=s)
    dict={'form':form}
    if request.method=='POST':
        form=studentmodelform(request.POST,instance=s)
        if form.is_valid():
            form.save()
            return addadmission(request)
    return render(request,'admissions/update.html',dict)

@login_required
@permission_required('amissons.delete_school')  #add delete change view 
def deletestudent(request,id):
    s=School.objects.get(id=id)
    s.delete()
    return addadmission(request)

class teacherread(ListView):
    model=teacher


class getteacher(DetailView):
    model=teacher


class addteacher(CreateView):
    model=teacher
    fields=('name','subject','exp','contact')

class updateteacher(UpdateView):
    model=teacher
    fields=  ('name','contact')  

class removeteacher(DeleteView):
    model=teacher    
    success_url = reverse_lazy('teachers')