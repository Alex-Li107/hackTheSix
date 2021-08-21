from django.shortcuts import render
from django.http import HttpResponse

#The code to excute when on the home page goes here
def index(request):
    return render(request, '16Pathways.html')

#When this will handle loading the code for the results page and ig processing the results of the survey 
def results(request):
    return HttpResponse('hello mens')