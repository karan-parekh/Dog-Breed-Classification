from os import name
from django.urls import path

from .views import upload_image_view, CallModel

urlpatterns = [
    path('', upload_image_view, name='upload-image'),
    path('model', CallModel.as_view(), name='class-model')
]