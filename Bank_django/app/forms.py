from django import forms
from .models import Data


class dataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = "__all__"