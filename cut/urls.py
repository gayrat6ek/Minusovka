from django.urls import path 

from .views import CutView,MixMusicView
urlpatterns = [
    path('mpcut/',CutView.as_view(),name='mpcut'),
    path('mix/',MixMusicView.as_view(),name='mix')
]