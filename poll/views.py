from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from . models import *
from . forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    post = Poll.objects.all()
    context = {'post':post}
    return render(request,'poll/index.html',context)

def vote(request,pk):
    votes=Poll.objects.get(pk=pk)
    vote=Vote()  
    context={'votes':votes,
             "vote":vote}
    if request.method == 'POST':
        vote=Vote(request.POST)
        select=request.POST['inlineRadioOptions']
        try:
            if select =='option1':
                votes.count_1 += int(1)
            elif select =='option2':
                votes.count_2 += int(1) 
        except Exception:
            return HttpResponse('Invalid form')              
        votes.save()  
        return redirect('index')       
    return render(request,'poll/vote.html',context)  

def results(request,pk):
    result=Poll.objects.get(pk=pk)
    context={'result':result}
    return render(request,'poll/results.html',context)    

