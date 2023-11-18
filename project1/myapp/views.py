from django.shortcuts import render
from .models import Person
# Create your views here.

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
    results = None
    print("hi")
    if request.method=='POST':
        user_input_text=str(request.POST['text'])
        gpt_output = gpt_turbo(user_input_text)
        results = gpt_output
        myinstaance = Person(userinputvalue = user_input_text, mycalvalue = results)
        myinstaance.save()
    return render(request, 'generate.html', {'result' : results})  