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

from django.core.mail import send_mail
from django.forms.models import model_to_dict
from django.core.mail import send_mail,EmailMessage

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



    
def cosbeauty_see_all(request):
    if request.method == 'GET':
        context = {}
        context['lg'] = request.COOKIES.get('language') or 'VI'
        context['domain'] = settings.DOMAIN
        try:
            context['obj'] = Website.objects.get(Count=1)
        except:
            context['obj'] = {}

        try:
            context['obj1'] = EC_story.objects.get(Order=1)
        except:
            context['obj1'] = {}

        context['list_Edit_dsdt_mb'] = Edit_dsdt.objects.all().order_by('Order')

        list_BlogPost =BlogPost.objects.all().order_by('-id')
        s = request.GET.get('s')
        if s:
            list_BlogPost = list_BlogPost.filter(Q(Title__icontains=s)).order_by('-id')
            context['s'] = s
        p = request.GET.get('p','1')
        context['p'] = p
        # Sử dụng Paginator để chia nhỏ danh sách (10 là số lượng mục trên mỗi trang)
        paginator = Paginator(list_BlogPost, settings.PAGE)
        # Lấy số trang hiện tại từ URL, nếu không mặc định là trang 1
        try:
            page_obj = paginator.get_page(p)  # tự xử lý PageNotAnInteger, EmptyPage
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
        context['list_BlogPost'] = page_obj
        context['page_obj'] = page_obj
        context['p'] = page_obj.number
        
        return render(request, 'sleekweb/client/cosbeauty_see_all.html', context, status=200)
    