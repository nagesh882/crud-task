from django import forms
from webapp.models import CRUD

# I have creted ModelForm to act as HTML form fields for perform CRUD operation on frontend side

class CRUDForm(forms.ModelForm):
    class Meta:
        model = CRUD
        fields = ('title', 'description')
        error_messages = {
            'title':{'required':'You must have to fill title of To Do is compulsory'},
            'description':{'required':'You must have to fill description'}
        }
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Title of To Do List'}),

            'description':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter description of To Do List', 'rows':5}),

            'created_at':forms.TextInput(attrs={'class':'form-control', 'readonly':True})
        }