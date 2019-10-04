#import cv2
import numpy as np
from PIL import Image
#from keras.models import load_model

def preprocess(image):
    #return preprocessed Image
    pass


def final_predict(image):
    model = load_model('model.h5')
    prediction = model.predict_classes(image)
    return prediction
