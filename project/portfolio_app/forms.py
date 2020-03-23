from django import forms
from .models import TodoList

class AddListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ["item", "completed"]
