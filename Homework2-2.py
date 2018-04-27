from numpy import *
import numpy as np  
from scipy import interpolate  
import pylab as pl  

d = 10
s = 10
Q = 10
T= 10
N = 10

K=N
I=0
C=0
Flag=0
x=0
q=0

while Flag==0:
    I=I+Q
    C=C+d
    if T>=K:
        T=K
        Flag=1;
    x = zeros((1,T),float)
    q= zeros((1,T),float)

    print( x )
    print( q )
