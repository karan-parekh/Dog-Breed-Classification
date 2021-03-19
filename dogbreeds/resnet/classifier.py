import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 
import cv2

from django.conf import settings
from keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input
import numpy as np

MODEL_PATH = os.path.join(settings.BASE_DIR, "resnet", "ml_models", "dogbreeds-v1-67.h5")


class DogBreedClassifier:

    BREEDS = ["beagle", "chihuahua", "doberman", "french_bulldog", "golden_retriever", "malamute", "pug", "saint_bernard", "scottish_deerhound", "tibetan_mastif"]

    def __init__(self):

        self.model = load_model(MODEL_PATH)

    def classify(self, img_path) -> str:
        image = self._preprocess(img_path)
        preds = self.model.predict(image)

        return self._decode_preds(preds)
    
    def _decode_preds(self, preds):
        preds = preds.tolist()[0]
        preds = list(map(lambda x: x * 100, preds))
        prob  = max(preds)
        idx   = preds.index(prob)

        return self.BREEDS[idx], prob

    @staticmethod
    def _preprocess(img_path):
        to_size    = (244, 244)
        orig_image = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2RGB)
        img        = cv2.resize(orig_image, to_size)

        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        return preprocess_input(x)
