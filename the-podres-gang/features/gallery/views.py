from django.http import HttpResponse
from features.gallery.models import Image
from django.views.generic import ListView, TemplateView, DetailView


class Home(ListView):
    queryset = Image.objects.order_by("-pub_date")
    template_name = "gallery/index.html"
    context_object_name = "images"

    def get_queryset(self):
        return super().get_queryset()


class About(TemplateView):
    template_name = "gallery/about.html"

# -x- # -x- # -x- # -x- # -x- # -x- # -x- # -x- #


class CreateImage(TemplateView):
    GREETINGS = "This is the create image page"

    def get(self, request):
        return HttpResponse(self.GREETINGS)


class DetailImage(DetailView):
    context_object_name = "image"
    model = Image
    template_name = "gallery/detail.html"
    # success_url = reverse("home")
    context_object_name = "image"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)    
