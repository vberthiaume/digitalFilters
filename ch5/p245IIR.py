import numpy as np
import scipy.signal
import matplotlib.pyplot as plt

Nx = 1024              # input signal length (nonzero portion)
Nh = 300               # FIR filter length


n = np.arange(Nx)

#input sinusoid
x = np.sin(n*2*np.pi*7/Nx)   

# zero-pad the input
zp = np.zeros(Nx/2) 
xzp = np.hstack((zp,x,zp)) 

#filter the input using a FIR "running sum" filter

A = np.array([1, -0.99])
#i had an error with B being only 1, so I made it an array... 
B = np.array([1, 0])
y = scipy.signal.lfilter(B,A,xzp)    # filtered output signal


# my plottings
Nzp = np.arange(len(xzp))

fig, axarr = plt.subplots(2, sharex=False)

axarr[0].plot(Nzp, xzp)
axarr[0].set_title('zero-padded input')
    
axarr[1].plot(Nzp, y)
axarr[1].set_title('filtered output')

plt.show()