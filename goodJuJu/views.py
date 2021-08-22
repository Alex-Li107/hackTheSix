from django.shortcuts import render
from django.http import HttpResponse

#The code to excute when on the home page goes here
def index(request):
    return render(request, 'index.html')

#When this will handle loading the code for the results page and ig processing the results of the survey 
def results(request):
    Sum = 0
    if request.method == 'POST':
        values = request.POST.getlist('val')
        for i in range (len(values)):
            Sum = Sum + values[i]
    else:
        values = {}
    return render(request, 'results.html', {'num': values})

def aboutus(request):
    return render(request, 'aboutUs.html')