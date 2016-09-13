################################ FIG J.11 P.705 ################################
# swanalmainplot.m
# Compare measured and theoretical frequency response.
# This script is invoked by swanalmainplot.m and family,
# and requires context set up by the caller.

import matplotlib.pyplot as plt
import numpy as np

def swanalmainplot(f, fs, gains, phases):
    
    fig, axarr = plt.subplots(2, sharex=False)

    fig.suptitle("Figure 2.7 p. 128", fontsize=14)
    
    #freqplot(f, gains, '*k', ttl, 'Frequency (Hz)', 'Gain')
    axarr[0].plot(f, gains, '*k')
    axarr[0].grid()
    axarr[0].set_title('Amplitude Response')
    #axarr[0].set_xlabel('Frequency (Hz)')
    axarr[0].set_ylabel('Gain');
    
    tar = 2 * np.cos(np.pi * f/fs)  # theoretical amplitude response
    axarr[0].plot(f, tar, '-k')
    
    tpr = -np.pi * f/fs             # theoretical phase response
    pscl = 1/(2*np.pi)              # convert radian phase shift to cycles
    axarr[1].plot(f, tpr*pscl,'-k')
    axarr[1].grid()
    axarr[1].set_title('Phase Response')
    axarr[1].set_xlabel('Frequency (Hz)')
    axarr[1].set_ylabel('Phase shift (cycles)')
    axarr[1].plot(f, phases*pscl, '*k')

    plt.show()