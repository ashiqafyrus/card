from django.shortcuts import render

# Create your views here.
def home(request):
     return render(request,'home.html')
def about(request):
     return render(request,'about.html')
def services(request):
     return render(request,'services.html')
def login(request):
     return render(request,'login.html')
def crmpage(request):
     return render(request,'crm.html')
def crmcontent(request):
     return render(request,'crmcontent.html')
def drag(request):
     return render(request,'drag.html')