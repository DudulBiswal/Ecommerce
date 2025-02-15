from django import forms
from .models import Product
from django.contrib.auth.models import User
class Productform(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class Userform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']