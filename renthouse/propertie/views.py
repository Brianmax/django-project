from django.shortcuts import render
from django.http import HttpResponse
from . forms import *
from . models import *
from django.views import generic
from django.views.generic.detail import DetailView
from django.views.generic import *
from django.urls import reverse_lazy


# Create your views here.


class IndexView(generic.ListView):
    model = Casa
    template_name = "index.html"
    context_object_name = "houses"

    #def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    print(context)
    #    return context

    
class CasaDetailView(DetailView):
    model = Casa
    template_name = "detail.html"
    context_object_name = "house"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["appartments"] = self.object.departamento_set.all()
        context["titulo"] = "Detail"
        return context


class PropertieCreateView(CreateView):
    model = Casa
    template_name = "create.html"
    form_class = FormHouse
    success_url = reverse_lazy("propertie:index")

    #   def form_valid(self, form):
    #    response = super().form_valid(form)
    #    return self.render_to_response(self.get_context_data(form = form))



def update(request, casa_id):
    form = FormHouse()
    if request.method == "POST":
        form = FormHouse(request.POST)
        if form.is_valid():
            house = Casa.objects.get(pk = casa_id)
            house.street = form.cleaned_data["street"]
            house.city = form.cleaned_data["city"]
            house.save()
    return render(request, "update.html", {"form": form})


class HouseUpdateView(UpdateView):
    model = Casa
    template_name = "update.html"
    form_class = FormHouse
    success_url = reverse_lazy("propertie:index")


def createAppartment(request, casa_id):
    appartment = Departamento()
    form = AppartmentForm()
    if request.method == "POST":
        form = AppartmentForm(request.POST)
        if form.is_valid():
            house = Casa.objects.get(pk = casa_id)
            appartment.price = form.cleaned_data["price"]
            appartment.rooms = form.cleaned_data["rooms"]
            appartment.size = form.cleaned_data["size"]
            appartment.casa = house
            appartment.save()
    return render(request, "createAppartment.html", {"form": form})


class CreateAppartmentView(CreateView):
    model = Departamento
    template_name = "createAppartment.html"
    form_class = AppartmentForm
    success_url = "succes.html"

    def form_valid(self, form):
        appartment = form.save(commit = False)
        print(self.kwargs["pk"])
        casaInstance = Casa.object.get(pk = self.kwargs["pk"])
        appartment.casa = casaInstance
        appartment.save()
        return super().form_valid(form)
    


class recibosLista(ListView):
    model = Recibo
    template_name = "recibos.html"
    context_object_name = "recibos"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["house"] = Casa.objects.get(pk = self.kwargs["pk"])
        return context
    
    def get_queryset(self):
        casa = Casa.objects.get(pk = self.kwargs["pk"])
        listaRecibos = casa.recibo_set.all()
        return listaRecibos


class CreateReciboView(CreateView):
    model = Recibo
    template_name = "createRecibo.html"
    form_class = ReciboForm
    
    def form_valid(self, form):
        recibo = form.save(commit=False)
        casa = Casa.objects.get(pk = self.kwargs["pk"])
        recibo.casa = casa
        recibo.save()
        return super().form_valid(form)


class DetailReciboView(DetailView):
    model = Recibo
    template_name = "detailRecibo.html"
    context_object_name = "recibo"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("This is kwargs")
        print(self.kwargs)
        recibo = Recibo.objects.get(pk = self.kwargs["pk_r"])
        context["recibo"] = recibo
        return context



#def index(request):
#    items = Casa.objects.all()
#    titulo = "Propiedades"
#    return render(request, "index.html", {"items": items, "titulo": titulo})


#def detail(request, casa_id):
#    house = Casa.objects.get(pk = casa_id)
#    appartments = house.departamento_set.all()
#    return render(request, "detail.html", {"house": house, 
#                                           "appartments": appartments})


#def create(request):
#    form = CreateHouse()
#    if request.method == "POST":
#        form = CreateHouse(request.POST)
#        if form.is_valid():
#            street = form.cleaned_data["street"]
#            city = form.cleaned_data["city"]
#            new_house = Casa()
#            new_house.street = street
#            new_house.city = city
#            new_house.save()
#    return render(request, "create.html", {"form": form})


#def recibosLista(request, casa_id):
#    house = Casa.objects.get(pk = casa_id)
#    recibos = house.recibo_set.all()
#    return render(request, "recibos.html",
#                  {"house": house, "recibos": recibos})


#def createRecibo(request, casa_id):
#    house = Casa.objects.get(pk = casa_id)
#    form = ReciboForm()
#    recibo = Recibo()
#    if request.method == "POST":
#        form = ReciboForm(request.POST)
#        if form.is_valid():
#            recibo.departamento = house
#            recibo.tipo = form.cleaned_data["tipo"]
#            recibo.emmited_date = form.cleaned_data["emitted_date"]
#            recibo.expired_date = form.cleaned_data["expired_date"]
#            recibo.save()
#    return render(request, "createRecibo.html", 
#                  {"form": form, "house": house})