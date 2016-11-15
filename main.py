import pygame
import struct
import wave
import time
import math

list = []

min_amp = 0
max_amp = 0
node = 0
anode = 0
pygame.init()

wave_file = wave.open("noise2.wav", "r")
frames = wave_file.getnframes()
pygame.mixer.music.load("noise2.wav")

pygame.mixer.music.play()

for i in xrange(frames):
    current_frame = wave_file.readframes(frames)
    ham = (int(struct.unpack("<h", current_frame)[0]))
    list.append(ham)
    if ham == 0:
       node += 1
    if ham > max_amp:
        max_amp = ham
    if ham < min_amp:
        min_amp = ham
print list[100]
for i in xrange(frames):
    update = list[i]
    list[i] = update *2
print list[100]