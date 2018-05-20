from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def GetSinglePost(request):
    return render(request, 'single.html')

def getProfile(request):
    return render(request, 'profileView.html')