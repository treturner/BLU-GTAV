import cv2
import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle

np_load_old = np.load
np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)
train_data = np.load('training_data/training_data.npy')
np.load = np_load_old

for data in train_data:
  img = data[0]
  choice = data[1]
  cv2.imshow('test', img)
  print(choice)
  if cv2.waitKey(25) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
    break