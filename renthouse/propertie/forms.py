from django import forms
from django.forms.widgets import NumberInput

class CreateHouse(forms.Form):
    street = forms.CharField(max_length=50)
    city = forms.CharField(max_length=50)


class AppartmentForm(forms.Form):
    price = forms.IntegerField()
    rooms = forms.IntegerField()
    size = forms.IntegerField()


class ReciboForm(forms.Form):
    tipo = forms.CharField(max_length=20)
    cantidad = forms.IntegerField()
    emitted_date = forms.DateField(widget=NumberInput(attrs = {"type": "date"}))
    expired_date = forms.DateField(widget=NumberInput(attrs = {"type": "date"}))