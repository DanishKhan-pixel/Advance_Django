from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    data={
        'title':'home ',
         'alpha':'software engineering',
    }
    return render(request, "index.html", data)
 
def dani(request):
    return HttpResponse("welcome again dani")

def ali(reques):
    return HttpResponse("welcom ali")


def alidetails(request, code):
    return HttpResponse(code)