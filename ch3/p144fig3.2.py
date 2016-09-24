import numpy as np
import scipy.signal
import matplotlib.pyplot as plt

def filterslow(B, A, x):
    # FILTERSLOW: Filter x to produce y = (B/A) x . Equivalent to 'y = filter(B,A,x)' using a slow (but tutorial) method.
    NB = len(B)
    NA = len(A)
    Nx = len(x)
    xv = x  #x(:)          # ensure column vector

    # do the FIR part using vector processing, store it in v
    v = B[0]*xv
    if NB > 1:
        for i in np.arange(1, min(NB,Nx)):
            xdelayed = np.hstack((np.zeros(i-1), xv[0:Nx-i+1]))
            v = v + B[i] * xdelayed
    
    # The feedback part is intrinsically scalar, so this loop is where we spend a lot of time.
    y  = np.zeros(len(x))               # pre-allocate y
    ac = -A[1:NA]                       # could be NA +1
    for i in range (Nx):                # loop over input samples
        t = v[i]                        # initialize accumulator
        if NA > 1:
            for j in range (NA-1):
                if i > j:
                    t += ac[j]*y[i-j]
                #else y(i-j) = 0
        y[i] = t
    #y = reshape(y, len(x)) # in case x was a row vector
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




