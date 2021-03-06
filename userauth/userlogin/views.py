from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# import model


@login_required(login_url="login/")
def home(request):
    return render(request,"home.html")

def registration(request):
    return render(request, "registration.html")


#-- new style

from django.views import View
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse


class RegistrationClass(View):
  template_name = "registration.html"
  
  def get(self, request, *args, **kwargs):
     return render(request, self.template_name)

  def post(self, request, *args, **kwargs):
   print "=="*40
   first_name =  request.POST.get("first_name", None)
   from blog.models import Blog 
   b = Blog(name=first_name)
   b.save() 

   return HttpResponse("Hi yoyoyoy")
