from pyexpat import model
from django import forms
from onlineshopapp.models import register
class editfm(forms.ModelForm):
    class meta:
        model=register
        fields="__all__"
        