from django.shortcuts import render
from django.views.generic import View

from .models import AdminMOdel
class AdminHome(View):
    def post(self,request):
        e = request.POST.get("email")
        i = request.POST.get("login")
        p = request.POST.get("pswd")
        print(e,i,p)
        try:
            data=AdminMOdel.objects.get(a_email=e,a_idno=i,a_password=p)
            if data:
                return render(request,"AdminHome.html")
            else:
                return render(request,"login.html")
        except:
            return render(request,"login.html")