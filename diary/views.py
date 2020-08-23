from django.shortcuts import render
from django.views import generic

app_name = "diary"
class IndexView(generic.TemplateView):
    template_name = "diary/index.html"

