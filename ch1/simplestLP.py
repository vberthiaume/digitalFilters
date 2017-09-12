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
import matplotlib.pyplot as plt

def simplestLP (x):  
    y = []
    y.append(x[0])
    for i in np.arange(len(x)-1):
        y.append(x[i] + x[i+1])

    return y;

# get an input sinusoid
Nx = 1024           
n = np.arange(Nx)
f = 1
x = np.sin(2*np.pi*f*n/Nx)   

# filter it
y = simplestLP(x)

# display the thing
fig, axarr = plt.subplots(2, sharex=False)

axarr[0].plot(n, x)
axarr[0].set_title('input')
    
axarr[1].plot(n, y)
axarr[1].set_title('filtered output')

#plt.plot(n, x)

plt.show()