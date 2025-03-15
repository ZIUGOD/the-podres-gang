from django import forms
from django.core.validators import MaxLengthValidator

class ImageForm(forms.Form):
    image_caption = forms.CharField(max_length=128, required=False, label="Título da imagem", validators=[MaxLengthValidator(128)])
    image = forms.ImageField(allow_empty_file=False, required=True, label="Escolha uma imagem")
    image_description = forms.CharField(max_length=512, required=False, label="Descrição da imagem", validators=[MaxLengthValidator(512)])
    image_tags = forms.CharField(max_length=512, required=False, label="Tags da imagem", validators=[MaxLengthValidator(512)])
    