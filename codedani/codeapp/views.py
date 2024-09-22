from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .form import userForm
from django.views.decorators.csrf import csrf_exempt

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

def blog(request):
    return render(request, "blog.html")

def contact(request):
    if request.method=="GET":
        output=request.GET.get('output')
    return render(request, "contact.html",{'output':output})

def alidetails(request, code):
    return HttpResponse(code)


# def userform(request):
#     # alpha=0
#     try:
#          # if request.method=='get':
#         #method firt
#          l1=int(request.get['num1'])
#          l2=int(request.get['num2'])

#         # second method
#         #  l1=int(request.GET.get('num1'))
#         #  l2=int(request.GET.get("numb2"))
#         print(l1+l2)
#         # alpha=l1+l2
        
#     except:
#         pass
    
#     return render(request, 'userform.html')

def userform(request):
    finals=0
    # fn=userForm() 
    try:
        
        #  if request.method=="POST":
        #method first
         l1=int(request.GET['num1'])
         l2=int(request.GET['num2'])
          # second method
        #  l1=int(request.GET.get('num1'))
        #  l2=int(request.GET.get("numb2"))
        #  print(l1+l2);
         finals=l1+l2


         url="/contact/?output={}".format(finals)
         return HttpResponseRedirect(url)
    
    except:
        pass
    # data = {
    #     'form': fn,
    #     'output': finals,
    # }
    return render(request, "userform.html" ,{'output':finals})
        

def calculator(request):
    c=''
    try:
        if request.method=='GET':
            l1=eval(request.GET['num1'])
            l2=eval(request.GET['num2'])
            operation=request.GET['operation']
            if operation=='+':
                c=l1+l2;
            elif operation=='-':
                c=l1-l2;
            elif operation=='*':
                c=l1*l2;
            elif operation=="/":
                c=l1/l2;
    
    
    
        

    except:
        c="Invalid operaton"
    print(c)
        
    return render(request, 'calculator.html',{'c':c})

def envodd(request):
    c=''
    if request.method=="POST":
        n=eval(request.POST.get('num1'))
        if n%2==0:
            c="Even number"
        else:
            c="odd number"
    
    return render(request,'checkevenodd.html',{'c':c})