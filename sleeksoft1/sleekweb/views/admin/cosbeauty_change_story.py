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


def cosbeauty_change_story(request):
    if request.method == 'GET':
        context = {}
        context['domain'] = settings.DOMAIN

        try:
            context['obj'] = EC_story.objects.get(Order=1)
        except:
            context['obj'] = {}

        
        if request.user.is_authenticated and request.user.is_superuser:
            return render(request, 'sleekweb/admin/cosbeauty_change_story.html', context, status=200)
        else:
            return redirect('login_admin')
    if request.method == 'POST':
        context = {}
        Media = request.FILES.get('Media')

        Media2 = request.FILES.get('Media2')

        Media3 = request.FILES.get('Media3')

        Content = request.POST.get('Content')
        Content_EN = request.POST.get('Content_EN')

        try:
            obj = EC_story.objects.get(Order=1)
            if Media:
                obj.Media = Media
            if Media2:
                obj.Media2 = Media2
            if Media3:
                obj.Media3 = Media3
            if Content:
                obj.Content=Content
            if Content_EN:
                obj.Content_EN=Content_EN
            obj.save()
        except:
            EC_story.objects.create(
                Media=Media,
                Media2=Media2,
                Media3=Media3,
                Content=Content,
                Content_EN=Content_EN,
                Order=1,
                )
        return redirect('cosbeauty_change_story')
    
