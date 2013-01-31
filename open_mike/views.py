__author__ = 'aramael'

from django.shortcuts import render

def home(request):

    return render(request,'front_page.html')