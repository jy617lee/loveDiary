from django import forms
from .models import Posting

class PostForm(forms.ModelForm):
    class Meta:
        model = Posting
        fields = ('text', )
