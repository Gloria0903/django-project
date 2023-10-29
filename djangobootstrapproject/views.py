from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def kuhusu(request):
    return render(request,'about.html')

def reach(request):
    return render(request,'contact.html')

def work(request):
    return render(request,'service.html')