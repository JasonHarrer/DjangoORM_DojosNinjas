from django.urls import path
from . import views

urlpatterns = [
                path('',            views.index),
                path('add-a-dojo',  views.add_a_dojo),
                path('add-a-ninja', views.add_a_ninja)
              ]
