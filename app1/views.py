from django.shortcuts import render

# Create your views here.
def naruto(request):
    return render(request,'naruto.html')

def hinata(request):
    return render(request,'hinata.html')