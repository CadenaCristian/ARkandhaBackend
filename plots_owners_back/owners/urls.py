from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import delete, listTypeOwner, list, getById, insert, update, delete

urlpatterns = [
    path('list', list),
    path('listTypeOwner', listTypeOwner),
    path('getById/<int:id>', getById),
    path('insert', insert),
    path('update', update),
    path('delete', delete)
]
