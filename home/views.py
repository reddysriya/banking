from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"index.html")
def apply(request):
    return render(request,"apply.html")
