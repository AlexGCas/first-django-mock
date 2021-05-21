from django import forms
from .models import Passenger, Airport, Flight



'''make forms below'''
class NewPassengerForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.choices = kwargs.pop('choices')
        super(NewPassengerForm, self).__init__(*args, **kwargs)
        self.fields['passenger'] = forms.ChoiceField(choices=self.choices)
    passenger = forms.ChoiceField()
