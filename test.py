import pygame
import struct
import wave
import time
import math
import winsound
import random


min_amp = 0
max_amp = 0
node = 0
anode = 0
pygame.init()
list = []

wave_file = wave.open("noise2.wav", "w")
sample_length = wave_file.getnframes()
sample_time = 3
volume_sample = float(0.5)
wave_file.setparams((2, 2, 44100, 132300, "NONE", "not compressed"))
nodes = 0
frequency = float(1000)
pi = float(math.pi)

for i in xrange(132300):
    value = (math.sin(pi*frequency*(i/float(44100)))*(volume_sample*3200))
    value += (math.sin(pi*frequency*(i/float(44100)))*(volume_sample*3200))
    value += (math.sin(pi*float(1/4) * frequency * (i / float(44100))) * (volume_sample * 3200))
    #value += (math.cos( (pi / 5) * frequency * (i / float(44100))) * (volume_sample * 3200))
    if value > node:
       nodes = value
    package = struct.pack("<h", value)
    list.append(package)

print nodes
list_str = ''.join(list)
wave_file.writeframes(list_str)
wave_file.close()
for x in range (0,10):
   winsound.PlaySound("noise2.wav", winsound.SND_FILENAME)

