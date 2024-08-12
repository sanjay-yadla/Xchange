from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('login/',views.loginpage, name='login-page'), 
    path('logout/',views.logoutpage, name='login-page'), 
    path('signup/',views.signuppage, name = 'signup-page'),
    path('home/',views.homepage, name = 'homepage'),
    path('profile/',views.profile, name='profile'),
    path('additem/',views.additem, name='additem'), 
    path('deleteitem/<int:id>/',views.deleteitem,name='deleteitem'),
]
