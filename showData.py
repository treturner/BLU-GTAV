import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2

# save np.load
np_load_old = np.load

# modify the default parameters of np.load
np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)

# call load_data with allow_pickle implicitly set to true
train_data = np.load('training_data.npy')

# restore np.load for future normal usage
np.load = np_load_old

for data in train_data:
  img = data[0]
  choice = data[1]
  cv2.imshow('test', img)
  print(choice)
  if cv2.waitKey(25) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
    break