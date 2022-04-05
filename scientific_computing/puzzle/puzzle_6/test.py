import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

SFREQ = 48000
t = np.linspace(0, 1, SFREQ)
f = 440
w = 2 * np.pi * f

sig = np.sin(w * t)
sig[:1000] = sig[:1000] * np.linspace(0, 1, 1000)
sig[-1000:] = sig[-1000:] * np.linspace(1, 0, 1000)
ton = np.concatenate((sig,sig))
wav.write('kacktask.wav', SFREQ, ton)
