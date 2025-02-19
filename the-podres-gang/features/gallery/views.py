from django.shortcuts import render
from django.http import HttpResponse
from .models import Image, User
from django.views.generic import TemplateView, ListView, View

class Home(ListView):
    model = Image
    context_object_name = "image"
    template_name = "gallery/index.html"
    paginate_by = 10
    


class About(View):
    GREETINGS = "This is the about page"

    def get(self, request):
        return HttpResponse(self.GREETINGS)


# -x- # -x- # -x- # -x- # -x- # -x- # -x- # -x- #


class CreateImage(View):
    GREETINGS = "This is the create image page"

    def get(self, request):
        return HttpResponse(self.GREETINGS)


class DetailImage(View):
    GREETINGS = "This is the detail image page"
    context_object_name = "image"

    def get(self, request):
        return HttpResponse(self.GREETINGS)
