from django.urls import path
from admissions import views
urlpatterns = [
    path('adm/', views.addadmission),
    path('newadm/',views.admissionreport),
    

]
