from django.shortcuts import render
from .models import Person
# Create your views here.

def welcome(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'about.html')

def contactus(request):
    result = None
    print('hi')
    if request.method=='POST':
        mynum=int(request.POST['number'])
        result = mynum*100
        print(mynum)
        myinstaance = Person(userinputvalue = mynum, mycalvalue = result)
        myinstaance.save()
    return render(request, 'contact.html', {'result' : result})

def generate(request):
    return render(request, 'generate.html')  