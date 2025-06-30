from django.db import models

# Create your models here.
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin

from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify

# Create your models here.


class User(AbstractUser):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Quản lý tài khoản Đăng Nhập"
    AbstractUser._meta.get_field('email').blank = False
    AbstractUser._meta.get_field('email').blank = False
    AbstractUser._meta.get_field('username').blank = False
    AbstractUser._meta.get_field('username').blank = False
    AbstractUser._meta.get_field('password').blank = False
    AbstractUser._meta.get_field('password').blank = False
    
    Avatar = models.ImageField(upload_to='user_image', default="user_image/user_empty.png", null=True,blank=True)
    Full_name = models.CharField('Họ và tên', max_length=255,blank=True, null=True)
    Phone_number = models.CharField('Số điện thoại', max_length=255,blank=True, null=True)
    OTP = models.CharField('Mã Otp',max_length=255, null=True,blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    class Meta:
        indexes = [
            models.Index(fields=['username']),
            models.Index(fields=['email']),
            models.Index(fields=['Full_name']),
        ]


class Website(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Thông tin trang web"
    
    Logo = models.ImageField(upload_to='Change_Website',null=True,blank=True)
    Phone_number = models.CharField('Số điện thoại', max_length=50,blank=True, null=True)
    Text_run = models.CharField('Chữ chạy', max_length=100,blank=True, null=True)
    Email = models.CharField('Email', max_length=50,blank=True, null=True)
    Count = models.IntegerField('Số bản ghi',blank=True, null=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

class Edit_lh(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Thông tin map"
    
    Address = models.CharField('Địa chỉ liên hệ', max_length=200,blank=True, null=True)
    Address_EN = models.CharField('Địa chỉ liên hệ EN', max_length=200,blank=True, null=True)
    Link_map = models.CharField('Link map', max_length=1000,blank=True, null=True)
    Count = models.IntegerField('Số bản ghi',blank=True, null=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

class Edit_dsdt(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Danh sách đối tác"
    
    Name = models.CharField('Tên phòng khám', max_length=200,blank=True, null=True)
    Address = models.CharField('Địa chỉ liên hệ', max_length=200,blank=True, null=True)
    Link = models.CharField('Link', max_length=200,blank=True, null=True)
    Photo = models.ImageField(upload_to='Edit_dsdt',null=True,blank=True)
    Order = models.IntegerField('Thứ tự',blank=True, null=True)
    Category = models.CharField('Danh mục', max_length=200,blank=True, null=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)



class BlogPost(models.Model):
    Title = models.CharField(max_length=350, blank=True, null=True)
    Title_EN = models.CharField(max_length=350, blank=True, null=True)
    Slug = models.SlugField(unique=True,max_length=350, blank=True, null=True)  # Thêm slug
    Content = RichTextUploadingField(blank=True, null=True)
    Content_EN = RichTextUploadingField(blank=True, null=True)
    Avatar = models.ImageField(upload_to='AVATAR_BLOG',null=True,blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

    def save(self, *args, **kwargs):
        if not self.Slug:
            base_slug = slugify(self.Title)
            slug = base_slug
            n = 1
            # Nếu slug đã tồn tại thì thêm số đuôi
            while BlogPost.objects.filter(Slug=slug).exists():
                slug = f"{base_slug}-{n}"
                n += 1
            self.Slug = slug
        super().save(*args, **kwargs)



# ////////////////////////////////////////////////////////////////////////////////////////////


class EC_home(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Thông tin trang chủ"
    
    Media = models.FileField(upload_to='Media_EC', null=True, blank=True)
    Order = models.IntegerField('Thứ tự',blank=True, null=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

class EC_about_us(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Thông tin về chúng tôi"
    
    Media = models.FileField(upload_to='Media_EC', null=True, blank=True)
    Content1 = models.TextField('Nội dung 1',blank=True, null=True)
    Content1_EN = models.TextField('Nội dung 1',blank=True, null=True)
    Content2 = models.TextField('Nội dung 2',blank=True, null=True)
    Content2_EN = models.TextField('Nội dung 2',blank=True, null=True)
    Media3 = models.FileField(upload_to='Media_EC', null=True, blank=True)
    Content3 = models.TextField('Nội dung 3',blank=True, null=True)
    Content3_EN = models.TextField('Nội dung 3',blank=True, null=True)
    Media4 = models.FileField(upload_to='Media_EC', null=True, blank=True)
    Content4 = models.TextField('Nội dung 4',blank=True, null=True)
    Content4_EN = models.TextField('Nội dung 4',blank=True, null=True)
    Order = models.IntegerField('Thứ tự',blank=True, null=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

class EC_commit(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Cam kết"
    
    Media = models.FileField(upload_to='Media_EC', null=True, blank=True)
    Title = models.CharField(max_length=350, blank=True, null=True)
    Title_EN = models.CharField(max_length=350, blank=True, null=True)
    Content = models.TextField('Nội dung',blank=True, null=True)
    Content_EN = models.TextField('Nội dung',blank=True, null=True)
    Order = models.IntegerField('Thứ tự',blank=True, null=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

class EC_story(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Thông tin trang Câu chuyện"
    
    Media = models.FileField(upload_to='Media_EC', null=True, blank=True)
    Media2 = models.FileField(upload_to='Media_EC', null=True, blank=True)
    Media3 = models.FileField(upload_to='Media_EC', null=True, blank=True)
    Content = models.TextField('Nội dung',blank=True, null=True)
    Content_EN = models.TextField('Nội dung',blank=True, null=True)
    Order = models.IntegerField('Thứ tự',blank=True, null=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    


