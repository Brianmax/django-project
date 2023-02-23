from django.urls import path

from . import views

app_name = "propertie"
urlpatterns = [
    path("", views.index, name = "index"),
    path("<int:casa_id>/", views.detail, name = "detail"),
    path("create/", views.create, name = "create"),
    path("<int:casa_id>/update/", views.update, name = "update"),
    path("", views.deleteItem, name = "deleteItem"),
    path("<int:casa_id>/createAppartment/", 
         views.createAppartment, name = "createAppartment")
]
