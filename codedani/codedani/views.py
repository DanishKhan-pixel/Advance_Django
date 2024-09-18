from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    data={
        'title':'home',
        'alpha':'software engineering', 
        'list':['ali','ahamad','khan'],
        'student_details':[
            {'name':'ali','phone':123456},
            {'name':'khan','phone':123456}
        ]
    } 
    return render(request, "index.html", data)
 
def dani(request):
    return HttpResponse("welcome again dani")

def ali(reques):
    return HttpResponse("welcom ali")


def alidetails(request, code):
    return HttpResponse(code)