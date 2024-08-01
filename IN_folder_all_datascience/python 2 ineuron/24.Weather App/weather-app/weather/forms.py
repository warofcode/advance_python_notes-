from django.forms import ModelForm, TextInput
from .models import City


class CityForm(ModelForm):
    class Meta:
        model = City  # database name in which the input must be stored
        fields = ['name']  # input field of the database
        widgets = {
            'name': TextInput(attrs={'class': 'input', 'placeholder': 'City Name'}),
        }  # updates the input class to have the correct Bulma class and placeholder
