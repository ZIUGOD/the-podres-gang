from django.contrib.auth.decorators import login_required, login_not_required
from django.urls import path
from features.gallery.views import CreateImage, DetailImage

urlpatterns = [
    path(
        "create/",
        login_required(CreateImage.as_view()),
        name="create_image",
    ),
    path(
        "<int:image_id>/",
        login_not_required(DetailImage.as_view()),
        name="detail_image",
    ),
]
