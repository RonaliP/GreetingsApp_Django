from django import forms
from .models import Users


class MessageForm(forms.ModelForm):
    class Meta:
        model=Users
        fields='__all__'
        labels={
            'Name':'YOUR NAME',
            'Message':'YOUR MESSAGE'
        }

