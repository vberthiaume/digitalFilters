# manual implementation of the simplest LP in python
# c++ code is
# double simplp (double *x, double *y, int M, double xm1)
# {
#     int n;
#     y[0] = x[0] + xm1;
#
#     for (n=1; n < M ; n++) {
#         y[n] = x[n] + x[n-1];
#     }
#     return x[M-1];
# }

import numpy as np
#import scipy.signal
import matplotlib.pyplot as plt

#get an input sinusoid
Nx = 1024           
n = np.arange(Nx)    
x = np.sin(n*2*np.pi*7/Nx)   

fig, axarr = plt.subplots(2, sharex=False)

axarr[0].plot(n, x)
axarr[0].set_title('zero-padded input')
    
axarr[1].plot(n, x)
axarr[1].set_title('filtered output')

plt.show()