import tensorflow as tf
import numpy as np
from PIL import Image
from picamera import PiCamera
from time import sleep

MODEL_DIRPATH = '../models/DIRNAME'

model = tf.keras.models.load_model(MODEL_DIRPATH)
cam = PiCamera()

while True:
    cam.capture('temp.jpg')
    img = Image.open('temp.jpg')
    arr = np.asarray(img)
    res = model.predict(np.array([arr, ]))
    print(res)
    sleep(1)
