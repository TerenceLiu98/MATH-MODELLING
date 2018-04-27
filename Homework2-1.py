import numpy as np  
from scipy import interpolate  
import pylab as pl  
x=[0 ,0.01,0.03,0.08,0.2,0.4,0.67, 0.85, 0.93, 0.9, 1.0]
q=[1000,1050,1150,1250,1350,1450,1550,1650, 1750,1850,2000]
xnew=np.linspace(0,10,101)  
pl.plot(x,q,"ro")  
  
for kind in ["nearest","zero","slinear","quadratic","cubic"]:
    f=interpolate.interp1d(x,y,kind=kind)  
    ynew=f(xnew)  
    pl.plot(xnew,qnew,label=str(kind))  
pl.legend(loc="lower right")  
pl.show() 
