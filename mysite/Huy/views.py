from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from . import forms
# Create your views here.

def indexview(request):
    return render(request,'index.html')

def registervieww(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html',{'form':form})

def formview(request):
    form1 = forms.FormName()
    return render(request, 'form.html', {'form1':form1})

def thanksview(request):
    return render(request, 'Thanks.html')



