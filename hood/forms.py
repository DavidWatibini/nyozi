from django import forms
from .models import *

# class NeighbourHoodForm(forms.ModelForm):
#     class Meta:
#         model = NeighbourHood
#         fields = ('user_id','hood_name','location_id')
#
# class MakePostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ('image_path','image_description','hood_id')
#
# class UploadForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields =('user','email_address','neighborhood_id')
#
# class BizForm(forms.ModelForm):
#     class Meta:
#         model = Business
#         fields =('business_name','user','neighborhood_id','business_email')
