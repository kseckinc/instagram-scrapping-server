# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .models import Account
import os

from .tasks import create_account, send_direct_message
from .forms import DirectMessageForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect


@login_required(login_url="/login/")
def index(request):
    banned = Account.objects.filter(isActive=False).count()
    data = Account.objects.all()
    all_count = data.count()
    
    context = {
        "accounts": data,
        "banned":banned,
        "active":all_count-banned,
        "bannedPrecentage":int((banned/all_count)*100) if banned != 0 else 0,
        "activePrecentage":int(((all_count-banned)/all_count)*100) if all_count != 0 else 0

    }
    context['segment'] = 'index'

    return render(request, 'index.html', context)

@login_required
def start_create(request):
    isOverride=request.POST.get('overide', '')
    minkey=request.POST.get('mink', '')
    maxkey=request.POST.get('maxk', '')
    minall=request.POST.get('mina', '')
    maxall=request.POST.get('maxa', '')
    proxy=request.POST.get('proxy', '')
    loop=request.POST.get('loop', '')
    if "account.lock" in os.listdir(os.getcwd()) and isOverride=='0' :
        return HttpResponse("A previous service running", content_type="text/plain")
    elif isOverride !='' and minkey !='' and maxkey !='' and minall !='' and maxall !='' and proxy !='' and loop !='' :
        open("account.lock","w")
        f=open("accountlog.txt","w")
        f.close()
        d={"keys_min":int(minkey),"keys_max":int(maxkey),"min":int(minall),"max":int(maxall)}
        for _ in range(int(loop)):
            create_account.delay(d, proxy)
        # os.system("python3 '%s/instanew2.py' %s %s %s %s %s %s " % (os.getcwd(),minkey,maxkey,minall,maxall,proxy,loop))
        return HttpResponse("Service Started", content_type="text/plain")
    else:
        return HttpResponse("Invalid Data", content_type="text/plain")

@login_required
def dm_create_view(request, username):
    account = Account.objects.filter(username=username).first()
    if not account:
        messages.warning(request, 'User not fount with %s' % username)
        return redirect('app:home')

    if request.method == 'POST':
        form = DirectMessageForm(request.POST)
        if form.is_valid():
            data = form.data
            open("dm.lock","w")
            f=open("dmlog.txt","w")
            f.close()
            d = {}
            d['sender'] = account.username
            d['password'] = account.password
            d['username'] = data.get('username')
            d['message'] = data.get('message')
            send_direct_message.delay(d)
            messages.success(request, 'messages sended successfully')
            return redirect('app:home')
        else:
            messages.danger(request, 'Invalid')
            return redirect('home')
    else:
        form = DirectMessageForm()
    return render(request, 'direct-message.html', {'form': form})

@login_required
def account_log(request):
    f = open(os.getcwd()+'/accountlog.txt', 'r')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="text/plain")
@login_required
def dm_log(request):
    f = open(os.getcwd()+'/dmlog.txt', 'r')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="text/plain")
    
@login_required
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))
