
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('frances.html', views.frances, name="frances"),
    path('italiano.html', views.italiano, name="italiano"),
    path('tecnico.html', views.tecnico, name="tecnico"),
    path('conversacional.html', views.conversacional, name="conversacional"),
    path('signup.html', views.signup, name="signup"),
]
