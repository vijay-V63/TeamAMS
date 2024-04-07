from django.urls import path
from . import views
urlpatterns = [
    path("",views.home),
    path('alumnisignup',views.alumnisignup),
    path('alumnilogin',views.alumnilogin),
    path('alumnimain',views.alumnimain),
    path('studentsignup',views.studentsignup),
    path('studentlogin',views.studentlogin),
    path('studentmain',views.studentmain),
    path('adminpanel',views.adminpanel),
    path('adminpage',views.adminpage),
]