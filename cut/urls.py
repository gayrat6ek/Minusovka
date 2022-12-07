from django.urls import path 

from .views import CutView
urlpatterns = [
    path('mpcut/',CutView.as_view(),name='mpcut')
]