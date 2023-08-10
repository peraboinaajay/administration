from django.contrib import admin
from admissions.models import School

# Register your models here.
#class StudentAdmin(admin.ModelAdmin):
 #   list_display=['id','name','founded_year','location']
class student(admin.ModelAdmin):
    list_display=['id','name','location','founded_year']

admin.site.register(School,student)