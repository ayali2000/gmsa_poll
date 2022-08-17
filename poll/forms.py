from django import forms
from . models import *
class Vote(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['Quest','Name_1','Name_2','image_1','image_2']