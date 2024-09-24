from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .form import userForm
from django.views.decorators.csrf import csrf_exempt
from codeapp.models import*

def homepage(request):
    ServiceData=Service.objects.all()
    # print(ServiceData)
    # for a in ServiceData:
        # print(a)
    data={
        'title':'home page ',
        'alpha':'software engineering', 
        'list':['ali','ahamad','khan'],
        'number':[1,2,3,4,5,6,7,8,9],
        "ServiceData": ServiceData,
        'student_details':[
            {'name':'ali','phone':123456},
            {'name':'khan','phone':123456},


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
        if request.POST.get('num1')=="":
            return render(request,'checkevenodd.html',{'error':True})

        n=eval(request.POST.get('num1'))
        if n%2==0:
            c="Even number"
        else:
            c="odd number" 
    return render(request,'checkevenodd.html',{'c':c})

def marksheet(request):
    
     if request.method == "POST":
            s1 = eval(request.POST.get('subject1', 0))  
            s2 = eval(request.POST.get('subject2', 0))
            s3 = eval(request.POST.get('subject3', 0))
            s4 = eval(request.POST.get('subject4', 0))
            # Calculate total marks
            total = s1 + s2 + s3 + s4
            # print(total)
            p=total*100/400;
            if p>=60:
                d="first dev"
            elif p>=40:
                d="second dev"
            elif p>30:
                d="third dev"
            else:
                d='fail'
            data={
                'total':total,
                'per':p,
                'dev':d
            }
            return render(request, 'marksheet.html',data)
     return render(request, 'marksheet.html')