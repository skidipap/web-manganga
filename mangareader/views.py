from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView 
from django.views.generic import ListView

from .models import MangaList

class MangaReaderView(ListView):
    model = MangaList
    template_name = "mangareader/mangareader.html"
    context_object_name = "manga_list"
