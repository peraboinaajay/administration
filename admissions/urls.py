from django.urls import path
from admissions import views
from admissions.views import teacherread
from admissions.views import  getteacher
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('adm/', views.addadmission),
    path('newadm/',views.admissionreport),
    path('delete/<int:id>',views.deletestudent),
    path('update/<int:id>',views.updatestudent),
    path('teacher/',login_required(teacherread.as_view()),name='listteacher'),
    path('getteacher/<int:pk>/',login_required(getteacher.as_view()),name='getteacher'),
    path('addteacher/',login_required(views.addteacher.as_view())),
    path('updateteacher/<int:pk>/',login_required(views.updateteacher.as_view())),
    path('remove/<int:pk>/',login_required(views.removeteacher.as_view())),
    

]
