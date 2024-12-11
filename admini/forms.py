from django import forms
from .models import Admin_comment

class Admin_form(forms.ModelForm):
  class Meta:
    model=Admin_comment
    fields=['title','comment']
