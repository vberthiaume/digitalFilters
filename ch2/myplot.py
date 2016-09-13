################################ FIG J.1 P.682 ################################

import numpy as np
import matplotlib.pyplot as plt

def myplot(xdata, ydata=xdata, sym='', ttl='', xlab='', ylab='', grd=1, lgnd='', linewidth=1, fontsize=12):
    """MYPLOT - Generic plot - compatibility wrapper for plot()"""

    #this was the default value for xdata, I have no idea what this means so we'll cross that bridge when we get there
    #if nargin<2, ydata=xdata; xdata = 0 : length(ydata)-1 ; end

    plt.plot(xdata, ydata, sym, 'linewidth', linewidth)

    if len(ttl)>0:
        title(ttl, 'fontsize', fontsize, 'fontname','helvetica')
    
    if len(ylab)>0:
        ylabel(ylab, 'fontsize', fontsize, 'fontname','helvetica');
    
    if len(xlab)>0:
        xlabel(xlab, 'fontsize', fontsize, 'fontname','helvetica');
    
    if grd:
        plt.grid('on')
    else:
        grid('off')
    
    plt.show()