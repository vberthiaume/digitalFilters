# this is the python version of the matlab code in figures 2.3 and 2.4 p.124-125

import numpy as np
import scipy.signal
import sys
import matplotlib.pyplot as plt

import freqplot

################################ FIG J.10 P.704 ################################
#swanalplot.m - plots needed by swanal.m
def swanalplot(t, s, f, k, y):  

    #subplot(2,1,1)
    #ttl = sprintf('Filter Input Sinusoid, f(%d)=%0.2f',k,f(k))
    #myplot(t,s,'*k',ttl)
    #tinterp = np.arange(0, t[end], (t(2)-t(1))/10)      # interpolated time axis
    #si = ampin*cos(2*pi*f(k)*tinterp+phasein)           # for plot
    #text(-1.5,0,'(a)')
    #plot(tinterp,si,'--k')

    #subplot(2,1,2)
    #ttl='Filter Output Sinusoid'
    #myplot(t,y,'*k',ttl)
    #text(-1.5,0,'(b)')

    #saveplot(sprintf('../eps/swanal-%d.eps',k))

    fig, axarr = plt.subplots(2, sharex=True)

    title     = '%s %d %s %0.2f' % ('Filter Input Sinusoid, f(', k, ') = ', f[k])
    axarr[0].set_title(title)
    axarr[0].plot(t, s, '*k')

    tinterp = np.arange(0, len(t), (t[2]-t[1])/10)                  # interpolated time axis
    si      = ampin * np.cos(2 * np.pi * f[k] * tinterp + phasein)  # for plot
    axarr[0].plot(tinterp,si,'--k')

    axarr[1].set_title('Filter Output Sinusoid')
    axarr[1].plot(t, y, '*k')

    plt.show()

################################ FIG J.11 P.705 ################################
# swanalmainplot.m
# Compare measured and theoretical frequency response.
# This script is invoked by swanalmainplot.m and family,
# and requires context set up by the caller.
def swanalmainplot(f, fs, gains, phases):
    
    fig, axarr = plt.subplots(2, sharex=False)
    
    #freqplot(f, gains, '*k', ttl, 'Frequency (Hz)', 'Gain')
    axarr[0].plot(f, gains, '*k')
    axarr[0].grid()
    axarr[0].set_title('Amplitude Response')
    axarr[0].set_xlabel('Frequency (Hz)')
    axarr[0].set_ylabel('Gain');
    
    tar = 2 * np.cos(np.pi * f/fs)   # theoretical amplitude response
    axarr[0].plot(f, tar, '-k')
    
    tpr = -np.pi * f/fs         # theoretical phase response
    pscl = 1/(2*np.pi)        # convert radian phase shift to cycles
    axarr[1].plot(f, tpr*pscl,'-k')
    axarr[1].grid()
    axarr[1].set_title('Phase Response')
    axarr[1].set_xlabel('Frequency (cycles)')
    axarr[1].set_ylabel('Phase shift (cycles)')
    axarr[1].plot(f, phases*pscl, '*k')

    plt.show()

    

################################ FIG 2.6 P.127 ################################
def mod2pi(x):
    # MOD2PI - Reduce x to the range [-pi,pi)
    y = x
    twopi = 2 * np.pi
    while y >= np.pi:
        y = y - twopi
    while y < -np.pi:
        y = y + twopi
    return y

################################ FIG 2.4 P.125 ################################
def swanal(t,f,B,A):

    ampin   = 1                                 # input signal amplitude
    phasein = 0                                 # input signal phase
    N       = len(f)                         # number of test frequencies
    gains   = np.zeros(N)                        # pre-allocate amp-response array
    phases  = np.zeros(N)                        # pre-allocate phase-response array

    if len(A)==1 : 
        ntransient = len(B)-1                # no. samples to steady state
    else : 
        error('Need to set transient response duration here')

    for k in range (len(f)):                 # loop over analysis frequencies
        s   = ampin*np.cos(2*np.pi*f[k]*t+phasein)    # test sinusoid
        y   = scipy.signal.lfilter(B,A,s)                     # run it through the filter
        yss = y[ntransient:len(y)]           # chop off transient
        
        # measure output amplitude as max (SHOULD INTERPOLATE):
        #[ampout, peakloc] = np.max(abs(yss))       # ampl. peak & index
        yss = abs(yss)
        ampout, peakloc = np.max(yss), np.argmax(yss) # ampl. peak & index	

        gains[k] = ampout/ampin                 # amplitude response
     
        if ampout < sys.float_info.epsilon:     # eps returns "machine epsilon"
            phaseout = 0                        # phase is arbitrary at zero gain
        else:
            sphase = 2*np.pi*f[k]*(peakloc+ntransient-1)

            # compute phase by inverting sinusoid (BAD METHOD):
            phaseout = np.arccos(yss[peakloc]/ampout) - sphase
            phaseout = mod2pi(phaseout)         # reduce to [-pi,pi)

        phases[k] = phaseout-phasein
        #swanalplot(t, s, f, k, y)                              # signal plotting script

    return gains, phases


################################ FIG 2.3 P.124 ################################
# swanalmain.m - simulated sine-wave analysis on the simplest lowpass filter:
# y(n) = x(n)+x(n-1)}

B               = [1,1]                         # filter feedforward coefficients
A               = [1]                             # filter feedback coefficients (none)
N               = 10.0                            # number of sinusoidal test frequencies
fs              = 1.0                             # sampling rate in Hz (arbitrary)
fmax            = fs/2                          # highest frequency to look at
df              = fmax/(N-1)                    # spacing between frequencies
f               = np.arange(0, fmax, df)        #sampled frequency axis
dt              = 1/fs                          # sampling interval in seconds
tmax            = 10.0                            # number of seconds to run each sine test
t               = np.arange(0, tmax, dt)        # sampled time axis
ampin           = 1                             # test input signal amplitude
phasein         = 0                             # test input signal phase
[gains, phases]  = swanal(t,f/fs,B,A)            # sine-wave analysis
swanalmainplot(f, fs, gains, phases)                                # final plots and comparison to theory  

