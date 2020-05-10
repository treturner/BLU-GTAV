import numpy as np
import pandas as pd
from random import shuffle

np_load_old = np.load
np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)
train_data = np.load('training_data/training_data.npy')
np.load = np_load_old

lefts = []
rights = []
forwards = []
fwdLeft = []
fwdRight = []
punches = []
fwdPunches = []
nothing = []

for data in train_data:
    img = data[0]
    choice = data[1]

    if choice == [0,0,1,0,0,0,0,0,0,0,0]:
        lefts.append([img,choice])
    elif choice == [1,0,0,0,0,0,0,0,0,0,0]:
        forwards.append([img,choice])
    elif choice == [0,0,0,1,0,0,0,0,0,0,0]:
        rights.append([img,choice])
    elif choice == [0,0,0,0,0,1,0,0,0,0,0]:
        fwdRight.append([img,choice])
    elif choice == [0,0,0,0,1,0,0,0,0,0,0]:
        fwdLeft.append([img,choice])
    elif choice == [0,0,0,0,0,0,0,0,1,0,0]:
        punches.append([img,choice])
    elif choice == [0,0,0,0,0,0,0,0,0,1,0]:
        fwdPunches.append([img,choice])
    elif choice == [0,0,0,0,0,0,0,0,0,0,1]:
        nothing.append([img,choice])

shuffle(forwards)
shuffle(lefts)
shuffle(rights)
shuffle(fwdLeft)
shuffle(fwdRight)
shuffle(punches)
shuffle(fwdPunches)
shuffle(nothing)

forwards = forwards[:len(fwdLeft)][:len(fwdRight)]
lefts = lefts[:len(forwards)]
rights = rights[:len(forwards)]
fwdLeft = fwdLeft[:len(forwards)]
fwdRight = fwdRight[:len(forwards)]
punches = punches[:len(forwards)]
fwdPunches = fwdPunches[:len(forwards)]
nothing = nothing[:len(forwards)]

final_data = forwards + lefts + rights + fwdRight + fwdLeft + punches + fwdPunches + nothing
shuffle(final_data)
print("Data balanced.")

np.save('training_data/training_data_balanced.npy', final_data)