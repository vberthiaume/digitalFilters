import numpy as np
import scipy.signal
import matplotlib.pyplot as plt

# Feedforward coeffs
g1 = 0.5**3 
B = [1, 0, 0, g1]             

# Feedback coefficients
g2 = 0.9**5 
A = [1, 0, 0, 0, 0, g2]         


Nfft  = 1024                        # FFT size
Nspec = 1+Nfft/2                    # Show only positive frequencies
f     = np.arange(0., Nspec)/Nfft   # Frequency axis
Xnum  = np.fft.fft(B, Nfft)         # Frequency response of FIR part
Xden  = np.fft.fft(A, Nfft)         # Frequency response, feedback part
X     = Xnum / Xden                 # Should check for divide by zero!



fig, axarr = plt.subplots(2, sharex=True)
axarr[0].plot(f, X[0:Nspec].real)
axarr[1].plot(f, X[0:Nspec].imag)

plt.show()


