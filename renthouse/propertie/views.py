from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . forms import *
from . models import *
def index(request):
    items = Casa.objects.all()
    return render(request, "index.html", {"items": items})


def detail(request, casa_id):
    house = Casa.objects.get(pk = casa_id)
    appartments = house.departamento_set.all()
    return render(request, "detail.html", {"house": house, 
                                           "appartments": appartments})


def create(request):
    form = CreateHouse()
    if request.method == "POST":
        form = CreateHouse(request.POST)
        if form.is_valid():
            street = form.cleaned_data["street"]
            city = form.cleaned_data["city"]
            new_house = Casa()
            new_house.street = street
            new_house.city = city
            new_house.save()
    return render(request, "create.html", {"form": form})


def update(request, casa_id):
    form = CreateHouse()
    if request.method == "POST":
        form = CreateHouse(request.POST)
        if form.is_valid():
            house = Casa.objects.get(pk = casa_id)
            house.street = form.cleaned_data["street"]
            house.city = form.cleaned_data["city"]
            house.save()
    return render(request, "update.html", {"form": form})


def deleteItem(request, casa_id):
    to_remove = Casa.objects.get(pk = casa_id)
    print("Delete operation has began")
    to_remove.delete()
    return render(request, "index.html")


def createLeaseholder(request, casa_id, departamento_id):
    pass


def createAppartment(request, casa_id):
    appartment = Departamento()
    form = Appartment()
    if request.method == "POST":
        form = Appartment(request.POST)
        if form.is_valid():
            house = Casa.objects.get(pk = casa_id)
            appartment.price = form.cleaned_data["price"]
            appartment.rooms = form.cleaned_data["rooms"]
            appartment.size = form.cleaned_data["size"]
            appartment.casa = house
            appartment.save()
    return render(request, "createAppartment.html", {"form": form})
