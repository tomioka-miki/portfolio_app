from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<list_id>', views.delete, name="delete"),
    path('uncomplete/<list_id>', views.uncomplete, name="uncomplete"),
    path('complete/<list_id>', views.complete, name="complete"),
    path('edit/<list_id>/<list_item>', views.edit, name="edit"),
]