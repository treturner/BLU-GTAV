import cv2
import lib
import numpy as np
import os
import time
from lib.direct_keys import PressKey
from lib.get_keys import key_check
from lib.grab_screen import grab_screen

w =  [1,0,0,0,0,0,0,0,0,0,0]
s =  [0,1,0,0,0,0,0,0,0,0,0]
a =  [0,0,1,0,0,0,0,0,0,0,0]
d =  [0,0,0,1,0,0,0,0,0,0,0]
wa = [0,0,0,0,1,0,0,0,0,0,0]
wd = [0,0,0,0,0,1,0,0,0,0,0]
sa = [0,0,0,0,0,0,1,0,0,0,0]
sd = [0,0,0,0,0,0,0,1,0,0,0]
h =  [0,0,0,0,0,0,0,0,1,0,0]
wh = [0,0,0,0,0,0,0,0,0,1,0]
nk = [0,0,0,0,0,0,0,0,0,0,1]

def keys_to_output(keys):
    output = [0,0,0,0,0,0,0,0,0,0,0]

    if 'W' in keys and 'A' in keys:
        output = wa
    elif 'W' in keys and 'D' in keys:
        output = wd
    elif 'S' in keys and 'A' in keys:
        output = sa
    elif 'S' in keys and 'D' in keys:
        output = sd
    elif 'H' in keys and 'W' in keys:
        output = wh
    elif 'W' in keys:
        output = w
    elif 'S' in keys:
        output = s
    elif 'A' in keys:
        output = a
    elif 'D' in keys:
        output = d
    elif 'H' in keys:
        output = h
    else:
        output = nk
    return output

file_name = 'training_data/training_data.npy'
if os.path.isfile(file_name):
    print('File exists, loading previous data...')
    np_load_old = np.load
    np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)
    training_data = list(np.load(file_name))
    np.load = np_load_old
else:
    print('File does not exist, starting fresh...')
    training_data = []

def main():
    for i in list(range(5))[::-1]:
        print(i+1)
        time.sleep(1)
    paused = False

    while True:
        if not paused:
            screen = grab_screen(region=(0,40,1000,800))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (80, 60))
            keys = key_check()
            output = keys_to_output(keys)
            training_data.append([screen, output])
            if len(training_data) % 500 == 0:
                print(len(training_data))
                np.save(file_name, training_data)

        keys = key_check()
        if 'T' in keys:
            if paused:
                paused = False
                print('Unpausing...')
                time.sleep(1)
            else:
                print('Pausing...')
                paused = True
                time.sleep(1)

main()