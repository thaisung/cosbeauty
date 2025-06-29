"""
URL configuration for luanvan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from django.contrib import admin
# from Data_Interaction.admin import admin_site
from django.urls import path

from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from django.urls import re_path,path


from django.views.generic.base import TemplateView
from django.conf.urls.static import serve

from django.views.generic import RedirectView

from django.contrib.auth import views as auth_views

from .views.client.login_client import *


from .views.client.select_kvmb_client import *
from .views.client.select_kvmn_client import *



from .views.admin.login_admin import *
from .views.admin.change_website_admin import *
from .views.admin.change_lh_admin import *
from .views.admin.change_dsdt_admin import *
from .views.admin.change_blog_admin import *
from .views.admin.user_admin import *

from .views.client.cosbeauty_home import *
from .views.client.cosbeauty_trademark import *
from .views.client.cosbeauty_contact import *
from .views.client.cosbeauty_about_us import *
from .views.client.cosbeauty_story import *
from .views.client.cosbeauty_see_all import *
from .views.client.cosbeauty_story_detail import *

from .views.admin.cosbeauty_change_home import *
from .views.admin.cosbeauty_change_about_us import *
from .views.admin.cosbeauty_change_story import *

from sleekweb.sitemaps import *
from django.contrib.sitemaps.views import sitemap

sitemaps_dict = {
    'static': StaticViewSitemap,
    'product': detail_product_Sitemap,
}

urlpatterns = [

    path('set-language/<str:lang_code>/', set_language, name='set_language'),
    path('', cosbeauty_home,name='cosbeauty_home'),
    path('contact', cosbeauty_contact,name='cosbeauty_contact'),
    path('about-us', cosbeauty_about_us,name='cosbeauty_about_us'),
    path('story', cosbeauty_story,name='cosbeauty_story'),
    path('story-all', cosbeauty_see_all,name='cosbeauty_see_all'),
    path('story-detail/<str:slug>/', cosbeauty_story_detail,name='cosbeauty_story_detail'),
    path('trademark', cosbeauty_trademark,name='cosbeauty_trademark'),

    path('change-home', cosbeauty_change_home,name='cosbeauty_change_home'),
    path('change-about-us', cosbeauty_change_about_us,name='cosbeauty_change_about_us'),
    path('change-commit', cosbeauty_change_commit,name='cosbeauty_change_commit'),
    path('remove-commit',cosbeauty_remove_commit,name='cosbeauty_remove_commit'),
    path('change-story', cosbeauty_change_story,name='cosbeauty_change_story'),


    # path('admin/', admin.site.urls),

    #api
    #endapi
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps_dict}, name='sitemap'),


    path('account/login', login_client,name='login_client'),

    


    path('north-partner', select_kvmb_client,name='select_kvmb_client'),
    path('southern-partner', select_kvmn_client,name='select_kvmn_client'),




    path('admin/login', login_admin,name='login_admin'),
    path('admin/logout', logout_admin,name='logout_admin'),


    path('admin/change-website',change_website_admin,name='change_website_admin'),

    path('admin/change-lh',change_lh_admin,name='change_lh_admin'),
    path('admin/change-dsdt-mb',change_lh_admin,name='change_lh_admin'),
    path('admin/change-dsdt',change_dsdt_admin,name='change_dsdt_admin'),
    path('admin/change-dsdt-remove',change_dsdt_remove_admin,name='change_dsdt_remove_admin'),
    path('admin/change-dsdt-order',change_dsdt_order_admin,name='change_dsdt_order_admin'),

    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('admin/change-blog', change_blog_admin, name='change_blog_admin'),
    path('admin/change-blog/add', change_blog_add_admin, name='change_blog_add_admin'),
    path('admin/change-blog/edit/<int:pk>/', change_blog_edit_admin, name='change_blog_edit_admin'),
    path('admin/change-blog/remove/<int:pk>/', change_blog_remove_admin, name='change_blog_remove_admin'),

    path('admin/user/edit/<int:pk>/', user_edit_admin,name='user_edit_admin'),
    path('admin/user/change-password/', user_change_password_admin,name='user_change_password_admin'),

]