# simplpm2.m - block-oriented version of simplpm1.m

import numpy as np
import scipy.signal

N = 10 			# length of test input signal
x = np.arange(1,N)	# test input signal
B = [1.0, 1.0]  	# feedforward coefficients
A = [1.0]      		# feedback coefficients (no-feedback case)


# PROCESS IT ALL IN ONE SHOT
y1 = scipy.signal.lfilter(B, A, x)       
print "all in one shot: ", y1

# PROCESS IT IN BATCHES
NB = N/2		# block length



# process block 1
#[y1, Sf] = scipy.signal.lfilter(B, A, x[1:NB])       


#the problem with stuff below is that i don't understand how to use lfilter in a block way. 
#apparently this is possible, see here:
#http://stackoverflow.com/questions/8922657/matlab-filter-with-scipy-lfilter

# process block 2
#y2 = scipy.signal.lfilter(B, A, x[NB+1:N], Sf)  
# print input and output for block 1
#for i in range (1, NB):   
#  disp(sprintf('x(%d)=%f\ty(%d)=%f',i,x(i),i,y1(i)));
# print input and output for block 2
#for i in range (NB+1, N):
#   disp(sprintf('x(%d)=%f\ty(%d)=%f',i,x(i),i,y2(i-NB)));




