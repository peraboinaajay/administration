from django.urls import path
from finance import views
urlpatterns = [
   
    path('fee/',views.feecollection),
    path('due/',views.feeduesreport),

]
