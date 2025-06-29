from django import forms
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['Title','Title_EN', 'Content','Content_EN','Avatar']

