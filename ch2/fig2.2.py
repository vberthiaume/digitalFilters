# fig2.2 p.123
# simplpm2.m - block-oriented version of simplpm1.m

import numpy as np
import scipy.signal

N = 10 			    # length of test input signal
x = np.arange(1,N)	# test input signal
B = [1.0, 1.0]  	# feedforward coefficients
A = 1.0      		# feedback coefficients (no-feedback case)

# PROCESS IT ALL IN ONE SHOT
y = scipy.signal.lfilter(B, A, x)       
print "all in one shot:", y

# PROCESS IT IN BATCHES
NB = N/2
# in matlab, indices start at 1, but in python they start at 0
y1, zf  = scipy.signal.lfilter(B, A, x[0:NB], zi = [0])	#we need to have a zi to get a zf
y2, zf2 = scipy.signal.lfilter(B, A, x[NB:N], zi = zf)	#we need to store the Zf2 somewhere, otherwise it just goes into y2  
print "in 2 shots:\t", y1, y2
