# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10wloY52_NCHPuh-ILrF4ac40smJmgfSg

1. INITIAL SOUND PREVIEW
2. ALLOCATING A TUNE TO EACH NUMBER
3. RANDOM NUMBER GENERATOR 
4. FIXED NO. OF CHANCES

***INITIAL SOUND PREVIEW:***

We will make the user to listen the tunes corresponding to each number from 0 to 9 in the sequence. It will be played only once.

***ALLOCATING A TUNE TO EACH NUMBER:***

In this we will be allocating a tune(or word which is famous in the institute) corresponding to each no. from 0 to 9. We will make an aray or list of all the tunes. 

When playing for the first time,the first prescribed sequence will be made randomly and will be fixed by using a particular permutation of the above list.

***RANDOM NUMBER GENERATOR***

We will take an input from the user, in which he/she will select the no of digits in it. Accordingly, the tunes will be played for that number for each digit.

This number will be generated using quantum computing.

Reference - https://thequantuminsider.com/2019/11/04/quantum-programming-101-16-qubit-random-number-generator-tutorial/

https://medium.com/@justinwritescrap/development-of-quantum-programs-for-use-on-mobile-devices-177ca3729963

https://www.sciencedirect.com/science/article/pii/S1319157822000283
"""

!pip install pygame

import os
print(os.getcwd())

!pip install gtts

from gtts import gTTS
from IPython.display import Audio
from IPython.display import display
import numpy as np
from numpy import random


list1 = np.array(["Sorted","Anndhi bahegi","CG","CP","Chaappo","Dasssi"])
# random.shuffle(list1)

for voice in list1 : 
      tts = gTTS("{}".format(voice)) 
      tts.save('1.wav')
      sound_file = '1.wav'
      wn = Audio(sound_file, autoplay=False) ##
      display(wn)##"""