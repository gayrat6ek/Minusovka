from django.urls import path

from .views import MusicView,HistoryView,KaraokeView,MinusListApiView,KaraokeListApiView,SearchView,CategoryView,CategoryNameView

urlpatterns = [ 
    path('music/',MusicView.as_view()),
    path('history/',HistoryView.as_view()),
    path('karaoke/make',KaraokeView.as_view()),
    path('karaoke/list',KaraokeListApiView.as_view()),
    path('minus/list',MinusListApiView.as_view()),
    path('search/list',SearchView.as_view()),
    path('category/<int:id>',CategoryView.as_view()),
    path('category/',CategoryNameView.as_view()),
]