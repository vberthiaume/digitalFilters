import numpy as np
import scipy.signal
import matplotlib.pyplot as plt

#comb filter from page 142
#g1 = 0.5 ** 3                       # Some specific coefficients, chosen to place all filter zeros at radius .5 
#g2 = 0.9 ** 5                       # and all filter poles at radius .9 in the complex z plane.
#B = [1, 0, 0, g1]                   # Feedforward coefficients, M1=3
#A = [1, 0, 0, 0, 0, g2]             # Feedback coefficients, M2=5
#N = 1000                            # Number of signal samples
#x = np.random.random(N)             # Random test input signal
#y = scipy.signal.lfilter(B,A,x)     



Nx = 1024              # input signal length (nonzero portion)
Nh = 128               # FIR filter length


n = np.arange(Nx)

#input sinusoid
x = np.sin(n*2*np.pi*7/Nx)   

# zero-pad the input
zp = np.zeros(Nx/2) 
xzp = np.hstack((zp,x,zp)) 

#filter the input using a FIR "running sum" filter
A = 1 
B = np.ones(Nh)
y = scipy.signal.lfilter(B,A,xzp)    # filtered output signal


# my plottings
Nzp = np.arange(len(xzp))

fig, axarr = plt.subplots(2, sharex=False)

axarr[0].plot(Nzp, xzp)
axarr[0].set_title('zero-padded input')
    
axarr[1].plot(Nzp, y)
axarr[1].set_title('filtered output')

plt.show()