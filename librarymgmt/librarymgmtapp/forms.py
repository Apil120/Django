from .models import User
from django import forms

class Userform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','member_id','borrowed_books']

