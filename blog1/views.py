from django.shortcuts import render
# from django.shortcuts import HttpResponse
from django.http import HttpResponse
def hello(request):
    return render(request,'home.html',{})

def contact(request):
    return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})