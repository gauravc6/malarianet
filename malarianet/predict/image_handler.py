import os
import cv2
import numpy as np
from PIL import Image
from flask import current_app

def preprocess(image):
    img = Image.open(image)
    img = np.array(img)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray,(48,48),cv2.INTER_AREA)
    blurred = cv2.bilateralFilter(resized,5,25,25)
    final_image = blurred.reshape(1,48,48,1)
    return final_image
