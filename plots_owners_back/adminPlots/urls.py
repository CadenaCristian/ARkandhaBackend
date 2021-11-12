from django.urls import path
from .views import delete, list, getPlotById, insert, update, listAllPlotsType, listOwners

urlpatterns = [
    path('list', list),
    path('getPlotById/<int:id>', getPlotById),
    path('listAllPlotsType', listAllPlotsType),
    path('listOwners', listOwners),
    path('insert', insert),
    path('update', update),
    path('delete', delete)
]
