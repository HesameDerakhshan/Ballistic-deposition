# BD Model
# version
# Date: 
# Copyleft 2019 Hesam Derakhshan, all left reserved.
# Reference:
# [1] A.-L. Barabasi and H. E. Stanley, Fractal Concept in Surface Growth (Cambridge University Press, 1995).

from random import randrange
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import math
import time
 
L         = 512                                 # Size of lattice
h         = np.zeros(L)                      # h[i] shows the height at i.
t          = 1                                      # The current time
t1       = 60*L                           # t change from 0 to t1

W_var = []
T         = []


H     = []
l     =range(0,L)


axes = plt.gca()
axes.set_xlim(0,L)
axes.set_ylim(0,350)

#line, = axes.plot(l, h, 'r-')



while (t<t1):                                    # Main loop of BD Model
	StepSize = round(1 + 0.01 * t)    # Size of the following loop
	for c in range(StepSize):
		i = randrange(L)                     # Select a random site
		h[i%L] = max(1 + h[i % L],     # Add a particle to the random selected site
				               h[(i-1) % L], h[(i+1) % L])
		t = t + 1                                  # Increase time    

#	if(t%50==0):
#		H.append(h)
#		print(H)
#		time.sleep(5)
#		plt.stackplot(l,H)
#		plt.legend(loc='upper left')
		
#		line.set_xdata(l)
#		line.set_ydata(h)
#		for i in range(len(l)):
		plt.scatter(l[i],h[i],color="black",s=0.55)	
#		plt.pause(1e-25)
#		time.sleep(0.0001)
 





#plt.stackplot(l,H)

plt.show()

