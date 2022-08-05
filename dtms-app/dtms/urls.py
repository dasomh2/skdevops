from django.urls import path

from . import views

urlpatterns = [
    path('', views.tableView, name='tableView'),

]