from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView 

class MangaReaderView(TemplateView):
    template_name = "mangareader/mangareader.html"
