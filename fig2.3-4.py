# this is the python version of the matlab code in figures 2.3 and 2.4 p.124-125

import numpy as np
import scipy.signal
import sys


import freqplot
import swanalplot as splot
import swanalmainplot as smain
  

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

################################ FIG 2.4 P.125 ################################
def swanal(t,f,B,A):

    ampin   = 1                                 # input signal amplitude
    phasein = 0                                 # input signal phase
    N       = len(f)                            # number of test frequencies
    gains   = np.zeros(N)                       # pre-allocate amp-response array
    phases  = np.zeros(N)                       # pre-allocate phase-response array

    if len(A)==1 : 
        ntransient = len(B)-1                   # no. samples to steady state
    else : 
        error('Need to set transient response duration here')

    for k in range (len(f)):                            # loop over analysis frequencies
        s   = ampin*np.cos(2*np.pi*f[k]*t+phasein)      # test sinusoid
        y   = scipy.signal.lfilter(B,A,s)               # run it through the filter
        yss = y[ntransient:len(y)+1]                      # chop off transient
        
        # measure output amplitude as max (SHOULD INTERPOLATE):
        yss     = np.abs(yss)
        ampout  = np.max(yss)                           # peak amplitude
        peakloc = np.argmax(yss)                        # index of the peak amplitude	

        gains[k] = ampout/ampin                         # amplitude response
     
        if ampout < sys.float_info.epsilon:             # eps returns "machine epsilon"
            phaseout = 0                                # phase is arbitrary at zero gain
        else:
            # compute phase by inverting sinusoid (BAD METHOD):
            #THERE IS SOMETHING WRONG WITH THIS CALCULATION, I CAN'T FIGURE IT OUT
            phaseout = np.arccos(yss[peakloc]/ampout) - 2*np.pi * f[k] * (peakloc+ntransient-1)
            phaseout = mod2pi(phaseout)                 # reduce to [-pi,pi)

        phases[k] = phaseout-phasein
        #splot.swanalplot(t, s, f, k, y, ampin, phasein)                              # signal plotting script

    return gains, phases


################################ FIG 2.3 P.124 ################################
# swanalmain.m - simulated sine-wave analysis on the simplest lowpass filter:
# y(n) = x(n)+x(n-1)}

#VARIABLES
B               = [1,1]                         # filter feedforward coefficients
A               = [1]                           # filter feedback coefficients (none)
N               = 10.0                          # number of sinusoidal test frequencies
fs              = 1.0                           # sampling rate in Hz (arbitrary)
fmax            = fs/2                          # highest frequency to look at
df              = fmax/(N-1)                    # spacing between frequencies
f               = np.arange(0, fmax+df/2, df)   # sampled frequency axis
dt              = 1/fs                          # sampling interval in seconds
tmax            = 10.0                          # number of seconds to run each sine test
t               = np.arange(0, tmax+dt/2, dt)   # sampled time axis

#ACTUAL ANALYSES
[gains, phases]  = swanal(t,f/fs,B,A)           # sine-wave analysis
smain.swanalmainplot(f, fs, gains, phases)      # final plots and comparison to theory  

