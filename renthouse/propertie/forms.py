from django import forms
from django.forms.widgets import NumberInput
from . models import *


class FormHouse(forms.ModelForm):
    class Meta:
        model = Casa

        fields = [
            "street",
            "city"
        ]

        labels = {
            "street": "Street",
            "city": "City"
        }

        widgets = {
            "street": forms.TextInput(),
            "city": forms.TextInput()
        }

class AppartmentForm(forms.ModelForm):
    class Meta:
        model = Departamento

        fields = [
            "price",
            "rooms",
            "size"
        ]
        labels = {
            "price": "Price",
            "rooms": "Rooms",
            "size": "Size"
        }
        widgets = {
            "price": forms.NumberInput(),
            "rooms": forms.NumberInput(),
            "size": forms.NumberInput()
        }

class ReciboForm(forms.Form):
    tipo = forms.CharField(max_length=20)
    cantidad = forms.IntegerField()
    emitted_date = forms.DateField(widget=NumberInput(attrs = {"type": "date"}))
    expired_date = forms.DateField(widget=NumberInput(attrs = {"type": "date"}))