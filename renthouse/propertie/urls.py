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
     
     
     path("<int:pk>/createAppartment/", 
         views.CreateAppartmentView.as_view(), name = "createAppartment"),
     
     path("<int:pk>/recibos", 
         views.recibosLista.as_view(), name = "recibos"),
     
     path("<int:pk>/recibos/createRecibo/",
         views.CreateReciboView.as_view(), name = "createRecibo"),
     
     path("<int:pk>/recibos/<int:pk_r>/", views.DetailReciboView.as_view(),
          name = "detailReciboView")
]
