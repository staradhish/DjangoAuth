from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^register/$', views.registration, name='register'),
    url(r'^reg/$', views.RegistrationClass.as_view()),
]

