import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

SFREQ = 4800


def note(s, freq):
    t = np.linspace(0, s / 2, SFREQ)
    w = 2 * np.pi * freq
    sig = np.sin(w * t)
    sig[:1000] = sig[:1000] * np.linspace(0, 1, 1000)
    sig[-1000:] = sig[-1000:] * np.linspace(1, 0, 1000)
    return sig


C = note(1, 523.251)
c = note(1, 261.626)
F = note(1, 698.456)
f = note(1, 349.228)
D = note(1, 587.330)
d = note(1, 293.665)
A = note(1, 880)
a = note(1, 440)
G = note(1, 783.991)
g = note(1, 391.995)
b = note(1, 466.164)
e = note(1, 329.628)
p = note(1, 0)

rythm = (
g, a, b, c, d, e, G, p, p, a, f, a, g, p, p, a, f, f, a, g, F, g, F, g, g, p, g, p, F, g, F, g, G, p, G, D, f, f, g, A,
p, f, g, G)
ton = np.concatenate(rythm)
wav.write('thomas_the_pain.wav', SFREQ * 2, ton)
