from django import forms
from .models import User


class UserRegistration(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['first_name', 'last_name', 'mobile', 'email']
        labels = {
            'first_name':'First Name',
            'last_name':'Last Name',
            'mobile':'Mobile Number',
            'email':'Email ID'
        }
        widgets = {
            'first_name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter Your First Name'
            }),
            'last_name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter Your Last Name'
            }),
            'mobile':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter Valid Mobile Mobile'
            }),
            'email':forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder':'Enter Valid Email Address'
            })

        }