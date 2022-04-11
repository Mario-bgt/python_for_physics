import numpy as np

print(np.mean(np.loadtxt('txt.txt', dtype=int)[-24:, int(len(np.loadtxt('txt.txt', dtype=int)[0])/3):int(len(np.loadtxt('txt.txt', dtype=int)[0])/3)+24]))
