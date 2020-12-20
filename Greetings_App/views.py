from django.shortcuts import render,redirect
from .forms import MessageForm
from  .models import Users
from datetime import datetime
# Create your views here.

def message_list(request):
    context={'message_list': Users.objects.all()}
    return render(request,"Message_list.html",context)

def message_form(request,id=0):     #m setting default id 0
    if request.method== "GET":    #if id=0 then request ll be about insert if not 0 the request ll be about update
        if id==0:
            form=MessageForm()
        else:
            user=Users.objects.get(pk=id)
            form=MessageForm(instance=user)
        return render(request,"message_form.html",{'form':form})
    else:
        if id==0:
            form = MessageForm(request.POST)
        else:
            user = Users.objects.get(pk=id)
            form=MessageForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
        return redirect('/greetings/list')

def message_delete(request,id):
    user = Users.objects.get(pk=id)
    user.delete()
    return redirect('/greetings/list')
