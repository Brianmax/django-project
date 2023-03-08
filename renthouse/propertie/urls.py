from django.urls import path
from . import views

app_name = "propertie"
urlpatterns = [
    path("", views.IndexView.as_view(), name = "index"),
    path("<int:pk>/", views.CasaDetailView.as_view(), name = "detail"),
    path("create/", 
         views.PropertieCreateView.as_view(), name = "create"),
    path("<int:pk>/update/", 
         views.HouseUpdateView.as_view(), name = "update"),
    path("", views.deleteItem, name = "deleteItem"),
    path("<int:pk>/createAppartment/", 
         views.CreateAppartmentView.as_view(), name = "createAppartment"),
    path("<int:casa_id>/recibos", 
         views.recibosLista, name = "recibos"),
    path("<int:casa_id>/recibos/createRecibo/",
         views.createRecibo, name = "createRecibo")
]
