from django import forms
from .models import *

class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        fields = ('user_id','hood_name','location_id')
