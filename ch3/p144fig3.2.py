import numpy as np
import scipy.signal
import matplotlib.pyplot as plt

def filterslow(B, A, x):
    # FILTERSLOW: Filter x to produce y = (B/A) x . Equivalent to 'y = filter(B,A,x)' using a slow (but tutorial) method.
    NB = len(B)
    NA = len(A)
    Nx = len(x)

    #first index of B contains gain for whole input x
    v = B[0] * x    
    
    #other indices in B contain gain for delayed input, ie, feedforward gains
    if NB > 1:
        # we loop until we run out of either feedforward gains or samples
        for k in np.arange(1, min(NB, Nx)):
            # to delay the input by i-1 samples, we simply insert i-1 0s in front of x 
            padding  = np.zeros(k - 1)
            xdelayed = np.hstack((padding, x[0 : Nx-k+1]))
            #having 0s at the front of xdelayed means that the corresponding samples in v will not be updated
            #because they were already processed on previous iterations
            v += B[k] * xdelayed
    
    # The feedback part is intrinsically scalar, so this loop is where we spend a lot of time.
    y  = np.zeros(len(x))              
    ac = A[1:NA]                        #so we just ignore A[0]?    
    
    # loop over input samples
    for i in range (Nx):                
        t = v[i]                        # initialize accumulator
        #if we have feedback gains
        if NA > 1:
            for k in range (NA-1):
                if i > k:
                    t -= ac[k]*y[i-k]
                #else y(i-k) = 0
        y[i] = t

    return y






N = 10000
x  = np.random.random(N)                            # random input signal
B  = np.random.random(101)                          # random coefficients
A  = np.hstack((1, 0.001*np.random.random(100)))    # random but probably stable

#tic 
yf = scipy.signal.lfilter(B, A, x)
#ft = toc
#tic 
yfs = filterslow(B, A, x)
#fst=toc


# my plottings
fig, axarr = plt.subplots(3, sharex=False)

axarr[0].plot(np.arange(N), x)
axarr[0].set_title('random numbers')
    
axarr[1].plot(np.arange(N), yf)
axarr[1].set_title('lfiltered random numbers')

axarr[2].plot(np.arange(N), yfs)
axarr[2].set_title('filtered slow random numbers')

plt.show()




