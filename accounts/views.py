from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from datetime import datetime

class Index(TemplateView):
    template_name = "accounts/index2.html"

index = Index.as_view()

class exercise_class(TemplateView):
    template_name = "accounts/exercise.html"
    def get(self, request, **kwargs):
        now = datetime.now()
        context = {
            "text": "TEST_EXERCISE_CLASS",
            "time": now,
        }
        return self.render_to_response(context)

def index_template(request):
    return render(request, "accounts/index.html")

def exercise(request):
    if request.method == "GET":
        now = datetime.now()
        context = {
            "text": "TEST_EXERCISE",
            "time": now,
        }
        return render(request, "accounts/exercise.html", context)

