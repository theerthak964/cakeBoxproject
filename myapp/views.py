from django.shortcuts import render,redirect
from django.views.generic import View

from myapp.models import CakeBox
from myapp.form import cakeboxForm



class cakeBoxCreateView(View):
    def get(self,request,*args,**kwargs):
        form=cakeboxForm
        return render(request,"cakeadd.html",{"form":form})
    def post(self,request,*args,**kwards):
        form=cakeboxForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("cake-list")
        return render(request,"cakeadd.html",{"form":form})
    
class CakeListView(View):
    def get(self,request,*args,**kwargs):
        qs=CakeBox.objects.all()
        return render(request,"cakelist.html",{"cakebox":qs})  

class CakeDetailsView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=CakeBox.objects.get(id=id)
        return render(request,"cakedetails.html",{"cake":qs})


class CakeEditView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        cake=CakeBox.objects.get(id=id)
        form=cakeboxForm(instance=cake)
        return render(request,"cakeedit.html",{"form":form})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        cake=CakeBox.objects.get(id=id)
        form=cakeboxForm(instance=cake,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("cakedetails",pk=id)
        return render(request,"cakeedit.html",{"form":form})    

class CakeDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        CakeBox.objects.get(id=id).delete()
        return redirect("cake-list")          
