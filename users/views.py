# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
class userView(module.View):
    # 注册一个用户
    def post(self,request):
        params = request.POST
        username = params.get('username')
        password = params.get('password')
        user = authenticate(username=username, password=password)
        user.save()
        return HttpResponse('注册成功')

    def login(self,request):
