from django.urls import path
from . import views

urlpatterns = [
                path('',                              views.index),
                path('add-a-dojo',                    views.add_a_dojo),
                path('add-a-ninja',                   views.add_a_ninja),
                path('delete-a-dojo/<int:dojo_id>',   views.delete_a_dojo),
                path('delete-a-ninja/<int:ninja_id>', views.delete_a_ninja)
              ]
