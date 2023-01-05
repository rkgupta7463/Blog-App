from django import forms
from dashboard.models import *


class ContactFm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"  
        widgets = {'name': forms.TextInput(attrs={'class':'form-control'}), 'email': forms.EmailInput(attrs={'class':'form-control'}),
                   'phone':forms.NumberInput(attrs={'class':'form-control'}), 'comments':forms.TextInput(attrs={'class':'form-control'})}
                   
