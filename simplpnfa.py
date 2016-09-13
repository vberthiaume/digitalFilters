import numpy as np
import scipy.signal
import swanalmainplot as smain
import matplotlib.pyplot as plt


#t       = np.arange(256)
#sinus   = np.sin(t)
#padding = np.zeros(512-len(t))
#Bzp     = np.concatenate((t, padding), axis=0) # zero-pad for the FFT
#sp      = np.fft.fft(Bzp)
#freq    = np.fft.fftfreq(t.shape[-1])
#plt.plot(freq, sp.real, freq, sp.imag)
#plt.show()




########################### FIGURE 2.11 P.134 ###########################

# simplpnfa.m - matlab program for frequency analysis of the simplest lowpass filter:
# y(n) = x(n)+x(n-1)}
# the way people do it in practice.


B       = [1,1]                        # filter feedforward coefficients
A       = [1]                          # filter feedback coefficients
N       = 128                          # FFT size = number of COMPLEX sinusoids
fs      = 1.0                          # sampling rate in Hz (arbitrary)
H       = np.fft.fft(B, N)             # since N is bigger than len(B), zero padding will be done to B

#if len(A)>1:                        
#    Azp = np.concatenate((A, np.zeros(N-len(A))), axis=0)  
#    # [Should guard against fft(Azp)==0 for some index]
#    H /= np.fft.fft(A, N)          # denominator from feedback coeffs

# Discard the frequency-response samples at negative frequencies, but keep the samples at dc and fs/2:
nnfi    = np.arange(N/2+1)         # nonnegative-frequency indices
Hnnf    = H[nnfi]                  # lose negative-frequency samples
f       = nnfi*fs/N                # frequency axis in Hz
gains   = np.abs(Hnnf)             # amplitude response
phases  = np.angle(Hnnf)           # phase response

smain.swanalmainplot(f, fs, gains, phases, "Figure 2.12 p.136") # final plots and comparison to theory