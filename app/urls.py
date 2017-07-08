# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""
from django.views.decorators.csrf import csrf_exempt
from django.urls import path, re_path
from app import views

app_name='app'

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    re_path(r'^.*\.html', views.pages, name='pages'),
    
    # The home page
    path('', views.index, name='home'),
    path(r'accounts/logs', views.account_log, name='account-logs'),
    path(r'accounts/create', csrf_exempt(views.start_create), name='startCreate'),
    path(r'dm/logs/', views.dm_log, name='dm-logs'),
    path(r'dm/<str:username>/', views.dm_create_view, name='dm-create'),
]
