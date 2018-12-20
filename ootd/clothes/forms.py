from django import forms
from .models import Closet, Thumb_closet
import requests

class ClosettForm(forms.ModelForm):
    class Meta:
        model = Closet
        fields = ('origin_img', )
