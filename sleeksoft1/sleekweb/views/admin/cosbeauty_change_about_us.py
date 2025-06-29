from ...models import *

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_list_or_404, get_object_or_404
from django.core.paginator import Paginator


from django.http import HttpResponse
import requests
import time

from django.db import models
from django.utils import timezone

import os

from datetime import datetime

from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout

from django.contrib.postgres.search import TrigramSimilarity
from django.db.models import Q
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from datetime import datetime
from django.contrib import messages
import random
import string
from django.contrib.auth import update_session_auth_hash
from datetime import datetime, timedelta
from django.utils.timezone import make_aware

# from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

import random
import string

import base64

import time
from django.http import JsonResponse

import re
import json

from django.conf import settings
from django.db.models import Q

import datetime

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


import base64


def cosbeauty_change_about_us(request):
    if request.method == 'GET':
        context = {}
        context['domain'] = settings.DOMAIN

        try:
            context['obj'] = EC_about_us.objects.get(Order=1)
        except:
            context['obj'] = {}

        context['list_commit'] = EC_commit.objects.all().order_by('id')
        
        if request.user.is_authenticated and request.user.is_superuser:
            return render(request, 'sleekweb/admin/cosbeauty_change_about_us.html', context, status=200)
        else:
            return redirect('login_admin')
    if request.method == 'POST':
        context = {}
        Media = request.FILES.get('Media')

        Content1 = request.POST.get('Content1')
        Content1_EN = request.POST.get('Content1_EN')

        Content2 = request.POST.get('Content2')
        Content2_EN = request.POST.get('Content2_EN')

        Media3 = request.FILES.get('Media3')
        Content3 = request.POST.get('Content3')
        Content3_EN = request.POST.get('Content3_EN')

        Media4 = request.FILES.get('Media4')
        Content4 = request.POST.get('Content4')
        Content4_EN = request.POST.get('Content4_EN')
        try:
            obj = EC_about_us.objects.get(Order=1)
            if Media:
                obj.Media = Media
            if Content1:
                obj.Content1=Content1
            if Content1_EN:
                obj.Content1_EN=Content1_EN
            if Content2:
                obj.Content2=Content2
            if Content2_EN:
                obj.Content2_EN=Content2_EN
            if Media3:
                obj.Media3 = Media3
            if Content3:
                obj.Content3=Content3
            if Content3_EN:
                obj.Content3_EN=Content3_EN
            if Media4:
                obj.Media4 = Media4
            if Content4:
                obj.Content4=Content4
            if Content4_EN:
                obj.Content4_EN=Content4_EN
            obj.save()
        except:
            EC_about_us.objects.create(
                Media=Media,
                Content1=Content1,
                Content1_EN=Content1_EN,
                Content2=Content2,
                Content2_EN=Content2_EN,
                Media3=Media3,
                Content3=Content3,
                Content3_EN=Content3_EN,
                Media4=Media4,
                Content4=Content4,
                Content4_EN=Content4_EN,
                Order=1,
                )
        return redirect('cosbeauty_change_about_us')
    
def cosbeauty_change_commit(request):
    if request.method == 'POST':
        context = {}
        Media = request.FILES.get('Media')
        Title = request.POST.get('Title')
        Title_EN = request.POST.get('Title_EN')
        Content = request.POST.get('Content')
        Content_EN = request.POST.get('Content_EN')
        id = request.POST.get('id')
        if id:
            try:
                obj = EC_commit.objects.get(id=id)
                if Media:
                    obj.Media = Media
                obj.Title = Title
                obj.Title_EN = Title_EN
                obj.Content = Content
                obj.Content_EN = Content_EN
                obj.save()
            except:
                print('Bản ghi ko tồn tại')
            return redirect('cosbeauty_change_about_us')
        else:
            EC_commit.objects.create(
                Media=Media,
                Title=Title,
                Title_EN=Title_EN,
                Content=Content,
                Content_EN=Content_EN
                )
            return redirect('cosbeauty_change_about_us')
        
def cosbeauty_remove_commit(request):    
    if request.method == 'POST':
        context = {}
        id = request.POST.get('id')
        try:
            obj = EC_commit.objects.get(pk=id)
            obj.delete()
        except:
            print('Xoá ko thành công')
        #     base_url = reverse('change_dsdt_admin')
        #     url = f"{base_url}?Category={Category}"
        #     return redirect(url)
        # base_url = reverse('change_dsdt_admin')
        # url = f"{base_url}?Category={Category}"
        return redirect('cosbeauty_change_about_us')
        
