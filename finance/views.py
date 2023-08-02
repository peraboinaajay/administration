from django.shortcuts import render

# Create your views here.
#function based views
def feecollection(request):
    return render(request,'finance/fee-collection.html')

def feeduesreport(request):
    return render(request,'finance/free-dues-reports.html')

