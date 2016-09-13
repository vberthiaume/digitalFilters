########################### FIGURE 2.11 P.134 ###########################
import numpy as np
import scipy.signal
import swanalmainplot as smain

# simplpnfa.m - matlab program for frequency analysis of the simplest lowpass filter:
# y(n) = x(n)+x(n-1)}
# the way people do it in practice.


B   = [1,1];                        # filter feedforward coefficients
A   = [1];                          # filter feedback coefficients
N   = 128;                          # FFT size = number of COMPLEX sinusoids
fs  = 1;                            # sampling rate in Hz (arbitrary)
padding = np.zeros(N-len(B))
Bzp = np.concatenate((B, padding), axis=0) # zero-pad for the FFT
H   = np.fft.fft(Bzp);              # len(Bzp) should be a power of 2

# we're not using this part here
if len(A)>1:                        
    Azp = np.concatenate((A, np.zeros(N-len(A))), axis=0);  
    # [Should guard against fft(Azp)==0 for some index]
    H /= np.fft.fft(A, N);          # denominator from feedback coeffs

# Discard the frequency-response samples at negative frequencies, but keep the samples at dc and fs/2:
nnfi    = np.arange(N/2+1);         # nonnegative-frequency indices
Hnnf    = H[nnfi];                  # lose negative-frequency samples
nnfb    = nnfi-1;                   # corresponding bin numbers
f       = nnfb*fs/N;                # frequency axis in Hz
gains   = np.abs(Hnnf);             # amplitude response
phases  = np.angle(Hnnf);           # phase response

smain.swanalmainplot(f, fs, gains, phases);                     # final plots and comparison to theory