from django.shortcuts import render
from django.http import HttpResponse



def dashboard(request):
    return render(request, 'crewcenter/dashboard.html')





def login(request):
    pass


def logout(request):
    pass