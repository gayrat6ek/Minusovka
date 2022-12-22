from django.urls import path 

from .views import CutView,MixMusicView,VolumeMixView
urlpatterns = [
    path('mpcut/',CutView.as_view(),name='mpcut'),
    path('mix/',MixMusicView.as_view(),name='mix'),
    path('volume/',VolumeMixView.as_view(),name='volume'),
]