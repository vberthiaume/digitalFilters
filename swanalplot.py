################################ FIG J.10 P.704 ################################
#swanalplot.m - plots needed by swanal.m
import matplotlib.pyplot as plt
import numpy as np

def swanalplot(t, s, f, k, y, ampin, phasein):  

    #subplot(2,1,1)
    #ttl = sprintf('Filter Input Sinusoid, f(%d)=%0.2f',k,f(k))
    #myplot(t,s,'*k',ttl)
    #tinterp = np.arange(0, t[end], (t(2)-t(1))/10)      # interpolated time axis
    #si = ampin*cos(2*pi*f(k)*tinterp+phasein)           # for plot
    #text(-1.5,0,'(a)')
    #plot(tinterp,si,'--k')

    #subplot(2,1,2)
    #ttl='Filter Output Sinusoid'
    #myplot(t,y,'*k',ttl)
    #text(-1.5,0,'(b)')

    #saveplot(sprintf('../eps/swanal-%d.eps',k))

    fig, axarr = plt.subplots(2, sharex=True)

    title     = '%s %d %s %0.2f' % ('Filter Input Sinusoid, f(', k, ') = ', f[k])
    axarr[0].set_title(title)
    axarr[0].plot(t, s, '*k')

    tinterp = np.arange(0, len(t), (t[2]-t[1])/10)                  # interpolated time axis
    si      = ampin * np.cos(2 * np.pi * f[k] * tinterp + phasein)  # for plot
    axarr[0].plot(tinterp,si,'--k')

    axarr[1].set_title('Filter Output Sinusoid')
    axarr[1].plot(t, y, '*k')

    plt.show()