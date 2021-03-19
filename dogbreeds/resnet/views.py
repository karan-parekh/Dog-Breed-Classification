import os

from django.shortcuts import get_object_or_404
from django.http import response, JsonResponse
from rest_framework.views import APIView
from django.shortcuts import render
from .forms import UploadImageForm
from .apps import ResnetConfig

# Create your views here.

def upload_image_view(request):
    context = {'form': UploadImageForm()}
    return render(request, 'upload_form.html', context=context)

class CallModel(APIView):

    def post(self, request):
        file_path = "temp.jpg"

        if request.method == 'POST':
            data = self.request.FILES['image']
            data = data.file.read()

            with open(file_path, 'wb+') as f:
                f.write(data)
                breed, probability = ResnetConfig.classifier.classify(file_path)
                response = {
                    'breed': breed,
                    'probability': probability
                }

            os.remove(file_path)
            return JsonResponse(response)

        else:
            return get_object_or_404

