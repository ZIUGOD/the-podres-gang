from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from features.gallery.models import Image, User
from django.views.generic import ListView, View


class Home(ListView):
    # model = Image # same as `queryset = Image.objects.all()`
    queryset = Image.objects.order_by("-pub_date")
    context_object_name = "images"
    template_name = (
        "gallery/index.html"  # mandatory, so dont use the "vanilla" object list
    )

    def get_queryset(self):
        return super().get_queryset()


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
    context_object_name = "image"
    model = Image
    template_name = "gallery/detail.html"

    def get_object(self, queryset=None):
        image = super().get_object_or_404(queryset)
        return image
    

    # def get_queryset(self, request):
    #     self.image = get_object_or_404(Image, pk=self.kwargs["image.id"])
    #     return self.image

    # def get(self, request):
    #         return HttpResponse(self.GREETINGS)
