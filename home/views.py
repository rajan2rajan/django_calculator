from cgitb import html
import re
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render
from .form import thanksform


# Create your views here.

def homepage(request):
    return HttpResponse("this is my first try")

def clothes_pant(request):
    return HttpResponse("here all the pant section are available")

# this is for dynamic link
def pant_design(requset,clothes):
    return HttpResponse(clothes)


def thankskforms(request):
    data = 0
    fn = thanksform()
    try:
        if request.method == 'post':
            data = {
            'forms':fn, 
            'name' : request.post.get("name"),
            'school': request.post.get('school'),
        }
        return render(request , "form.html" , {"data":fn})
    except:
        pass
    return render(request , "/form.html" , {"data":fn})



def submitform(request):
    return HttpResponse(request)


def calculator(request):
    c=''
    try:
        if request.method=="post":
            value1 = eval(request.POST.get('value1')),
            oper = request.POST.get('oper'),
            value2 = eval(request.POST.get('value2')),
            if oper == "+":
                c =  value1 + value2;

            elif oper == "-":
                c= value1-value2;

            elif oper == "*":
                c= value1*value2;

            elif oper == "/":           
                c= value1/value2;
        else:
            pass
        
    except:
        c = print('error occured')
    
    return render(request , "calculator.html",{"c":c} )
    
    