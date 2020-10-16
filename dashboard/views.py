from django.shortcuts import render
from django.contrib.auth.models import User,auth
# Create your views here.
def dash(request):
    return render(request,'dashboard.html')
