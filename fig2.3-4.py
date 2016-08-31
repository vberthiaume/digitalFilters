# this is the python version of the matlab code in figures 2.3 and 2.4 p.124-125

# swanalmain.m - simulated sine-wave analysis on the simplest lowpass filter:
# y(n) = x(n)+x(n-1)}

B       = [1,1];                        # filter feedforward coefficients
A       = 1;                            # filter feedback coefficients (none)
N       = 10;                           # number of sinusoidal test frequencies
fs      = 1;                            # sampling rate in Hz (arbitrary)
fmax    = fs/2;                         # highest frequency to look at
df      = fmax/(N-1);                   # spacing between frequencies
f       = 0:df:fmax;                    # sampled frequency axis
dt      = 1/fs;                         # sampling interval in seconds
tmax    = 10;                           # number of seconds to run each sine test
t       = 0:dt:tmax;                    # sampled time axis
ampin   = 1;                            # test input signal amplitude
phasein = 0;                            # test input signal phase
[gains,phases] = swanal(t,f/fs,B,A);    # sine-wave analysis
swanalmainplot;                         # final plots and comparison to theory




#SIMULATED SINE WAVE ANALYSIS
def swanal(t,f,B,A):

    ampin   = 1                 # input signal amplitude
    phasein = 0                 # input signal phase
    N       = length(f)         # number of test frequencies
    gains   = zeros(1,N)        # pre-allocate amp-response array
    phases  = zeros(1,N)        # pre-allocate phase-response array

    if length(A)==1 : 
        ntransient=length(B)-1  # no. samples to steady state
    else : 
        error('Need to set transient response duration here')

    for k in range (length(f)):             # loop over analysis frequencies
        s = ampin*cos(2*pi*f(k)*t+phasein)  # test sinusoid
        y = filter(B,A,s)                   # run it through the filter
        yss = y[ntransient:length(y)]       # chop off transient
        
        # measure output amplitude as max (SHOULD INTERPOLATE):
        [ampout,peakloc] = max(abs(yss))        # ampl. peak & index
        gains(k) = ampout/ampin                 # amplitude response
     
        if ampout < eps:        # eps returns "machine epsilon"
            phaseout=0          # phase is arbitrary at zero gain
        else:
            sphase = 2*pi*f(k)*(peakloc+ntransient-1)

            # compute phase by inverting sinusoid (BAD METHOD):
            phaseout = acos(yss(peakloc)/ampout) - sphase
            phaseout = mod2pi(phaseout)     # reduce to [-pi,pi)

     
        phases(k) = phaseout-phasein
        swanalplot # signal plotting script

    return gains, phases
