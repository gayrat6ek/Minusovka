from django.urls import path

from .views import MusicView,MinusView ,HistoryView

urlpatterns = [ 
    path('music/',MusicView.as_view()),
    path('minus/',MinusView.as_view()),
    path('history/',HistoryView.as_view()),
]