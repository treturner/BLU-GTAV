import numpy as np
from grabscreen import grab_screen
import cv2
import time
from getkeys import key_check
from directkeys import PressKey
import os

w = [1,0,0,0,0,0,0,0,0]
s = [0,1,0,0,0,0,0,0,0]
a = [0,0,1,0,0,0,0,0,0]
d = [0,0,0,1,0,0,0,0,0]
wa = [0,0,0,0,1,0,0,0,0]
wd = [0,0,0,0,0,1,0,0,0]
sa = [0,0,0,0,0,0,1,0,0]
sd = [0,0,0,0,0,0,0,1,0]
nk = [0,0,0,0,0,0,0,0,1]

def keys_to_output(keys):
    '''
    Convert keys to a ...multi-hot... array
     0  1  2  3  4   5   6   7    8
    [W, S, A, D, WA, WD, SA, SD, NOKEY] boolean values.
    '''
    output = [0,0,0,0,0,0,0,0,0]

    if 'W' in keys and 'A' in keys:
        output = wa
    elif 'W' in keys and 'D' in keys:
        output = wd
    elif 'S' in keys and 'A' in keys:
        output = sa
    elif 'S' in keys and 'D' in keys:
        output = sd
    elif 'W' in keys:
        output = w
    elif 'S' in keys:
        output = s
    elif 'A' in keys:
        output = a
    elif 'D' in keys:
        output = d
    else:
        output = nk
    return output

# Sets file name and path for training_data
file_name = 'training_data.npy'
if os.path.isfile(file_name):
    print('File exists, loading previous data...')
    training_data = list(np.load(file_name))
else:
    print('File does not exist, starting fresh...')
    training_data = []


def main():
    # Count down timer
    for i in list(range(5))[::-1]:
        print(i+1)
        time.sleep(1)

    paused = False
    # Captures the screen
    while True:

        PressKey(0x11)

        if not paused:
            # Main game screen (IV)
            screen = grab_screen(region=(0,40,1000,800))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (200, 160))
            # Key input (DV)
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

        # # Displays screens
        # # Shows and moves mainscreen
        # cv2.imshow('window',screen)
        # cv2.moveWindow('window', 790, 0)
        # if cv2.waitKey(25) & 0xFF == ord('q'):
        #     cv2.destroyAllWindows()
        #     break

main()