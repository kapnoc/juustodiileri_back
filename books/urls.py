from django.urls import path

from . import controlers

app_name = "books"
urlpatterns = [
    # path('', views.index, name='index'),
    path('ocr/', controlers.ocr_controler, name='ocr'),
]
