from django.urls import path 
from .views import MangaReaderView

urlpatterns = [
        path('', MangaReaderView.as_view(), name='mangareader')
]
