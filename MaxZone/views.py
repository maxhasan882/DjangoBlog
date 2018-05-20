from django.shortcuts import render

def home(request):
    return render(request, 'Prepare.html')

def GetSinglePost(request):
    return render(request, 'Prepare.html')