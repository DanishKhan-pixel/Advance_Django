from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    data={
        'title':'home',
        'alpha':'software engineering', 
        'list':['ali','ahamad','khan'],
        'number':[1,2,3,4,5,6,7,8,9],
        'student_details':[
            {'name':'ali','phone':123456},
            {'name':'khan','phone':123456}
        ]
    } 
    return render(request, "index.html", data)
 
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, "about.html")


def alidetails(request, code):
    return HttpResponse(code)