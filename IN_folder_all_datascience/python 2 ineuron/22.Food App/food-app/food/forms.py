from django import forms
from .models import Food


class ListForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['food_item', 'quantity', 'calories']
