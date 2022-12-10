from django.urls import path

from .views import MusicView,MinusView ,HistoryView,KaraokeView

urlpatterns = [ 
    path('music/',MusicView.as_view()),
    path('minus/',MinusView.as_view()),
    path('history/',HistoryView.as_view()),
    path('karaoke/',KaraokeView.as_view()),
]