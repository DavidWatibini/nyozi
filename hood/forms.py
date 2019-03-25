from django import forms
from .models import *

class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        fields = ('user_id','hood_name','location_id')

class MakePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image_path','image_description','hood_id')
