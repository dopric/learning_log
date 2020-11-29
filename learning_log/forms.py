from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        fields= ['name']
        labels = ['name']