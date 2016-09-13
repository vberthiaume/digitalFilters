import numpy as np
import scipy.signal
import matplotlib.pyplot as plt

#comb filter from page 142
g1 = 0.5 ** 3                       # Some specific coefficients
g2 = 0.9 ** 5
B = [1, 0, 0, g1]                   # Feedforward coefficients, M1=3
A = [1, 0, 0, 0, 0, g2]             # Feedback coefficients, M2=5
N = 1000                            # Number of signal samples
x = np.random.random(N)             # Random test input signal
y = scipy.signal.lfilter(B,A,x)     # Matlab and Octave compatible

# my plottings
fig, axarr = plt.subplots(2, sharex=False)

axarr[0].plot(np.arange(N), x)
axarr[0].set_title('random numbers')
    
axarr[1].plot(np.arange(N), y)
axarr[1].set_title('filtered random numbers')

plt.show()

