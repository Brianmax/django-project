from django import forms


class CreateHouse(forms.Form):
    street = forms.CharField(max_length=50)
    city = forms.CharField(max_length=50)


class Appartment(forms.Form):
    price = forms.IntegerField()
    rooms = forms.IntegerField()
    size = forms.IntegerField()