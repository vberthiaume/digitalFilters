import numpy as np
import scipy.signal
import matplotlib.pyplot as plt
import matlab as matlab
from plot_zplane import zplane


    

# Feedforward coeffs
g1 = 0.5**3 
B = [1, 0, 0, g1]             

# Feedback coefficients
g2 = 0.9**5 
A = [1, 0, 0, 0, 0, g2]         


zeros, poles, gain = matlab.tf2zp(B,A)
zplane(zeros,poles)



fig, axarr = plt.subplots(2, sharex=True)
axarr[0].plot(f, X[0:Nspec].real)
axarr[1].plot(f, X[0:Nspec].imag)

plt.show()


