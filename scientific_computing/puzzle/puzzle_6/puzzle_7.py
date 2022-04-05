import numpy as np
import scipy.io.wavfile as wav
import random

SFREQ = 4800


def note(s, freq):
    t = np.linspace(0, s, SFREQ)
    w = 2 * np.pi * freq
    sig = np.sin(w * t)
    sig[:1000] = sig[:1000] * np.linspace(0, 1, 1000)
    sig[-1000:] = sig[-1000:] * np.linspace(1, 0, 1000)
    return sig


A = note(1, 440)
B = note(1, 880)
C = note(1, 660)
D = note(1, 550)
oktave = A + B
oktave = oktave / np.max(abs(oktave))

quinte = A + C
qunite = quinte / np.max(abs(quinte))

gterz = A + D
gterz = gterz / np.max(abs(gterz))

p = note(1, 0)


def reine_stimmung(n, m, l):
    i = n * oktave + m * qunite + l * gterz
    return i


rythm = []
l = ('a', 'b', 'c', 'd', 'e', 'f','g','h','i')
for i in l:
    a = random.randint(1, 4)
    b = random.randint(1, 4)
    c = random.randint(1, 4)
    print(a,b,c)
    l = reine_stimmung(a, b, c)
    rythm.append(l)

ton = np.concatenate(rythm)
wav.write('notes.wav', SFREQ, ton)
