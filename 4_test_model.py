import cv2
import keras
import numpy as np
import os
import time
from lib.direct_keys import PressKey, ReleaseKey, W, A, S, D, H, SHIFT
from lib.get_keys import key_check
from lib.grab_screen import grab_screen
from keras.models import load_model

WIDTH = 80
HEIGHT = 60
model_name = 'proportionate.h5'

model_path = 'saved_models/' + model_name
model = load_model(model_path)

def forw():
  PressKey(W)
  ReleaseKey(A)
  ReleaseKey(S)
  ReleaseKey(D)
  ReleaseKey(H)
  PressKey(SHIFT)

def back():
  ReleaseKey(W)
  ReleaseKey(A)
  PressKey(S)
  ReleaseKey(D)
  ReleaseKey(H)
  
def left():
  ReleaseKey(W)
  PressKey(A)
  ReleaseKey(S)
  ReleaseKey(D)
  ReleaseKey(H)

def right():
  ReleaseKey(W)
  ReleaseKey(A)
  ReleaseKey(S)
  PressKey(D)
  ReleaseKey(H)

def forw_left():
  PressKey(W)
  PressKey(A)
  ReleaseKey(S)
  ReleaseKey(D)
  ReleaseKey(H)
  PressKey(SHIFT)

def forw_right():
  PressKey(W)
  ReleaseKey(A)
  ReleaseKey(S)
  PressKey(D)
  ReleaseKey(H)
  PressKey(SHIFT)

def back_left():
  ReleaseKey(W)
  PressKey(A)
  PressKey(S)
  ReleaseKey(D)
  ReleaseKey(H)

def back_right():
  ReleaseKey(W)
  ReleaseKey(A)
  PressKey(S)
  PressKey(D)
  ReleaseKey(H)

def punch():
  PressKey(W)
  ReleaseKey(A)
  ReleaseKey(S)
  ReleaseKey(D)
  PressKey(H)
  PressKey(SHIFT)

def forw_punch():
  PressKey(W)
  ReleaseKey(A)
  ReleaseKey(S)
  ReleaseKey(D)
  PressKey(H)
  PressKey(SHIFT)

def main():
  for i in list(range(5))[::-1]:
    print(i+1)
    time.sleep(1)

  while True:
    screen = grab_screen(region=(0,40,1000,800))
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    screen = cv2.resize(screen, (80, 60))

    prediction = model.predict([screen.reshape(-1,WIDTH,HEIGHT,1)])[0]
    print(prediction)
    moves = list(np.around(prediction))

    if moves == [1,0,0,0,0,0,0,0,0,0,0]:
      forw()
    elif moves == [0,1,0,0,0,0,0,0,0,0,0]:
      back()
    elif moves == [0,0,1,0,0,0,0,0,0,0,0]:
      left()
    elif moves == [0,0,0,1,0,0,0,0,0,0,0]:
      right()
    elif moves == [0,0,0,0,1,0,0,0,0,0,0]:
      forw_left()
    elif moves == [0,0,0,0,0,1,0,0,0,0,0]:
      forw_right()
    elif moves == [0,0,0,0,0,0,1,0,0,0,0]:
      back_left()
    elif moves == [0,0,0,0,0,0,0,1,0,0,0]:
      back_right()
    elif moves == [0,0,0,0,0,0,0,0,1,0,0]:
      punch()
    elif moves == [0,0,0,0,0,0,0,0,0,1,0]:
      forw_punch()

main()