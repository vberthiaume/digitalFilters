#MATLAB CODE
#x = linspace(0,10);
#y1 = sin(x);
#y2 = sin(5*x);

#figure
#subplot(2,1,1);
#plot(x,y1)

#subplot(2,1,2);
#plot(x,y2)



#MATPLOTLIB CODE
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10, 400)
y1 = np.sin(x)
y2 = np.sin(5*x)

f, axarr = plt.subplots(2, sharex=True)
axarr[0].plot(x, y1)
axarr[1].plot(x, y2)

plt.show()