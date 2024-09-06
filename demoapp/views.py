from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import faces
# Create your views here.
def demo(request):
    obj=place.objects.all()
    res=faces.objects.all()
    return render(request,"index.html",{'result':obj,'output':res})


#def addition(request):
 #    x=int(request.GET['num1'])
 #   y=int(request.GET['num2'])
 #   res=x+y
 #   res1=x-y
 #   res2=x*y
 #   res3=x/y
# return render(request,"result.html",{'result':res,'result':res1,'result':res2,'result':res3})



