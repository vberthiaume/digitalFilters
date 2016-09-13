################################ FIG 2.6 P.127 ################################
def mod2pi(x):
    # MOD2PI - Reduce x to the range [-pi,pi)
    y = x
    twopi = 2.0 * np.pi
    while y >= np.pi:
        y -= twopi
    while y < -np.pi:
        y += twopi
    return y


######################## FIG 2.10 P.133 ######################
import numpy as np
import scipy.signal

def swanalc(t,f,B,A):
    # SWANALC - Perform COMPLEX sine-wave analysis on the digital filter having transfer function
    # H(z) = B(z)/A(z)

    ampin   = 1                      # input signal amplitude
    phasein = 0                      # input signal phase
    N       = len(f)                 # number of test frequencies
    gains   = np.zeros(N)            # pre-allocate amp-response array
    phases  = np.zeros(N)            # pre-allocate phase-response array

    if len(A)==1:
        ntransient = len(B)-1
    else: 
        error('Need to set transient response duration here')

    # loop over analysis frequencies
    for k in range(len(f)):                     
        s           = ampin * np.exp(1j * 2*np.pi * f[k] * t + phasein) # test sinusoid
        y           = scipy.signal.lfilter(B, A, s)                     # run it through the filter
        yss         = y[ntransient+1:len(y)+1]                          # chop off transient
        ampout      = np.mean(np.abs(yss))                              # avg instantaneous amplitude
        gains[k]    = ampout/ampin                                      # amplitude response sample
        sss         = s[ntransient+1:len(y)+1]                          # align with yss
        angles      = np.angle(yss*sss.conj())
        
        for i in range(len(angles)):
            angles[i] = mod2pi(angles[i])    

        phases[k]   = np.mean(angles)

    return gains, phases
