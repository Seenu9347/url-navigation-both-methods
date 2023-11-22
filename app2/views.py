from django.shortcuts import render

# Create your views here.
def sasuke(request):
    return render(request,'sasuke.html')

def sakura(request):
    return render(request,'sakura.html')
