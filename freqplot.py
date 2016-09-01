################################ FIG J.2 P.683 ################################
import matplotlib.pyplot as plt

def freqplot(fdata, ydata, symbol='', ttl='', xlab='Frequency (Hz)', ylab=''):
    """ FREQPLOT - Plot a function of frequency. See myplot for more features."""
    
    #not sure what this means
    #if nargin<2, fdata=0:length(ydata)-1; end

    plt.plot(fdata, ydata, symbol);
    plt.grid()
    plt.title(ttl)
    plt.ylabel(ylab)
    plt.xlabel(xlab);