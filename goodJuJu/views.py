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
            "cluster": "Anthropology, Sociology, & Psychology",
            "job1": "Psychiatrist",
            "job2": "Therapist",
            "job3": "Social/Human Service Worker",
            "job4": "Child Welfare Worker"
        }
    elif Sum >= 71 and Sum <= 75:
        values_dict =  {
            "perty": "ENFJ",
            "cluster": "Social Work",
            "job1": "Counsellor",
            "job2": "Family Mediator",
            "job3": "Child Protection Services Worker",
            "job4": "Human Rights Lawyer"
        }
    elif Sum >= 66 and Sum <= 70:
        values_dict =  {
            "perty": "ISFJ",
            "cluster": "Health Sciences",
            "job1": "Family Physician",
            "job2": "Kinesiologist",
            "job3": "Nurse",
            "job4": "Community Relations Officer"
        }
    elif Sum >= 61 and Sum <= 65:
        values_dict =  {
            "perty": "INTJ",
            "cluster": "Computer Sciences",
            "job1": "Data Scientist",
            "job2": "Web Developer",
            "job3": "Computer System Analysts",
            "job4": "Software Engineer"
        }
    elif Sum >= 55 and Sum <= 60:
        values_dict =  {
            "perty": "INFP",
            "cluster": "Linguistics & Writing Studies",
            "job1": "Journalist",
            "job2": "Freelance Writer/Poet",
            "job3": "Translator",
            "job4": "Lexicographer"
        }
    elif Sum >= 50 and Sum <= 54:
        values_dict =  {
            "perty": "ENTJ",
            "cluster": "Political Science",
            "job1": "Lobbyist",
            "job2": "Sales Manager",
            "job3": "Government Official",
            "job4": "Budget Analyst"
        }
    elif Sum >= 45 and Sum <= 49:
        values_dict =  {
            "perty": "ESFJ",
            "cluster": "Education",
            "job1": "Elementary/High School Teacher",
            "job2": "Daycare Administrator",
            "job3": "School Guidance Counsellor",
            "job4": "Health Educator"
        }
    elif Sum >= 40 and Sum <= 44:
        values_dict =  {
            "perty": "ENFP",
            "cluster": "Media & Communication Studies",
            "job1": "Digital Marketer",
            "job2": "Graphic Designer",
            "job3": "Photographer",
            "job4": "Social Media Manager"
        }
    elif Sum >= 35 and Sum <= 39:
        values_dict =  {
            "perty": "ISTJ",
            "cluster": "Engineering",
            "job1": "Civil Engineer",
            "job2": "Engineering Consultant",
            "job3": "Product Tester",
            "job4": "Logistician"
        }
    elif Sum >= 30 and Sum <= 34:
        values_dict =  {
            "perty": "INTP",
            "cluster": "Mathematics",
            "job1": "Academic Researcher",
            "job2": "Pure Mathematician",
            "job3": "Cryptographer",
            "job4": "Actuary"
        }
    elif Sum >= 25 and Sum <= 29:
        values_dict =  {
            "perty": "ISFP",
            "cluster": "Creative Art & Design",
            "job1": "Professional Musician",
            "job2": "Landscape Designer",
            "job3": "Animator",
            "job4": "Stylist"
        }
    elif Sum >= 20 and Sum <= 24:
        values_dict =  {
            "perty": "ISTP",
            "cluster": "Athletics",
            "job1": "",
            "job2": "",
            "job3": "",
            "job4": ""
        }
    elif Sum >= 15 and Sum <= 19:
        values_dict =  {
            "perty": "ENTP",
            "cluster": "Physical Science",
            "job1": "Astrophysicist",
            "job2": "Patent Examiner",
            "job3": "Microbiologist",
            "job4": "Product Developer"
        }
    elif Sum >= 10 and Sum <= 14:
        values_dict =  {
            "perty": "ESFP",
            "cluster": "Performing Arts",
            "job1": "Actor/Actress",
            "job2": "Dancer",
            "job3": "Musical Theatre Performer",
            "job4": "Choreographer"
        }
    elif Sum >= 5 and Sum <= 9:
        values_dict =  {
            "perty": "ESTJ",
            "cluster": "Law Enforcement",
            "job1": "",
            "job2": "",
            "job3": "",
            "job4": ""
        }
    elif Sum >= 0 and Sum <= 4:
        values_dict =  {
            "perty": "ESTP",
            "cluster": "Entrepreneurship & Business Studies",
            "job1": "",
            "job2": "",
            "job3": "",
            "job4": ""
        }
    
    

    
    return render(request, 'results.html', values_dict)

def aboutus(request):
    return render(request, 'aboutUs.html')