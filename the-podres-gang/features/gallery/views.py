from django.urls import reverse
from features.gallery.models import Image
from django.views.generic import CreateView, ListView, TemplateView, DetailView


class Home(ListView):
    queryset = Image.objects.order_by("-pub_date")
    template_name = "gallery/index.html"
    context_object_name = "images"

    def get_queryset(self):
        return super().get_queryset()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_is_authenticated"] = self.request.user.is_authenticated
        context["total_images"] = Image.objects.count()
        return context


class About(TemplateView):
    template_name = "gallery/about.html"

# -x- # -x- # -x- # -x- # -x- # -x- # -x- # -x- #

class CreateImage(CreateView):
    model = Image
    fields = ["caption", "image", "description"]
    template_name = "gallery/create_image.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("home")
    

class DetailImage(DetailView):
    context_object_name = "image"
    model = Image
    template_name = "gallery/detail.html"
    context_object_name = "image"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)    
