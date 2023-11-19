from django.shortcuts import render, redirect
from .models import Person
# Create your views here.



from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required



from openai import OpenAI
client = OpenAI(api_key="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")


def gpt_turbo(strval):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": strval}
        ]
)

    return str(completion.choices[0].message.content)

@login_required
def welcome(request):
    return render(request, 'index.html')

@login_required
def aboutus(request):
    return render(request, 'about.html')

@login_required
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

@login_required
def generate(request):
    results = None
    print("hi")
    if request.method=='POST':
        user_input_text=str(request.POST['text'])
        gpt_output = gpt_turbo(user_input_text)
        results = gpt_output
        myinstaance = Person(userinputvalue = user_input_text, mycalvalue = results)
        myinstaance.save()
    return render(request, 'generate.html', {'result' : results})  


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('welcome') # Change 'welcome' to the name of your home page URL
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('welcome') # Change 'welcome' to the name of your home page URL
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_fun(request):
    logout(request)
    return redirect('login')

