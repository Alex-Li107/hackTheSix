from django.shortcuts import render
from django.http import HttpResponse

#The code to excute when on the home page goes here
def index(request):
    return render(request, 'index.html')

#When this will handle loading the code for the results page and ig processing the results of the survey 
def results(request):
    values = ""
    Sum = 0
    if request.method == 'POST':
        values = request.POST.getlist('val')
        #values is a list of strings, change the values into an int and sum them up so aaren can find out ur personailty
        for i in range (len(values)):
            Sum = Sum + int(values[i])
        #you dont need this if u summing it all up. Delete when ur done
    
    #if statements to determine personality
    if Sum >= 76:
        values_dict =  {
            "perty": "INFJ",
            "job1": "test"
        }
    elif Sum < 76 and Sum >= 71:
        values_dict =  {
            "perty": "ENFJ",
            "job1": "testt"
        }

    
    return render(request, 'results.html', values_dict)

def aboutus(request):
    return render(request, 'aboutUs.html')