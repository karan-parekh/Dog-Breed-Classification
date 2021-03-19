from django.apps import AppConfig
from .classifier import DogBreedClassifier


class ResnetConfig(AppConfig):
    name = 'resnet'
    classifier = DogBreedClassifier()
