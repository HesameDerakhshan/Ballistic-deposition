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

L         = 256                                  # Size of lattice
h         = np.zeros(L)                      # h[i] shows the height at i.

t          = 1                                      # The current time
t1       = 100000*L                           # t change from 0 to t1

W_var = []
T         = []


while (t<t1):                                    # Main loop of BD Model
	StepSize = round(1 + 0.01 * t)    # Size of the following loop
	for c in range(StepSize):
		i = randrange(L)                     # Select a random site
		h[i%L] = max(1 + h[i % L],     # Add a particle to the random selected site
				               h[(i-1) % L], h[(i+1) % L])
		t = t + 1                                  # Increase time    
	
	W_var.append(np.var(h))
	T.append(t)
	

#step    = 0
#L
#T_log1 = []
#W_log1 = []
#T_log2 = []
#W_log2 = []
#T_log3 = []
#W_log3 = []


#log of W_var and T array
#for i in range(len(T)):
#	ti = math.log10(T[i])
#	wi = math.log10(W_var[i])
#	if (ti<=9):
#		T_log1.append(ti)
#		W_log1.append(wi)
#	elif (ti<=5.11):
#		T_log2.append(ti)
#		W_log2.append(wi)
#	elif(ti> 5.11):
#		T_log3.append(ti)
#		W_log3.append(wi)
#		
#		
#conver list to array	
#T_log1 = np.asarray(T_log1)
#W_log1 = np.asarray(W_log1)
#T_log2 = np.asarray(T_log2)
#W_log2 = np.asarray(W_log2)
#T_log3 = np.asarray(T_log3)
#W_log3 = np.asarray(W_log3)

		
#linre curve fiting function 	
#slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(T,W_log1)
#slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(T_log2, W_log2)
#slope3, intercept3, r_value3, p_value3, std_err3 = stats.linregress(T_log3, W_log3)


#print("beta1: ",slope1,"beta2: ",slope2,"beta3: ",slope3)


np.savetxt(str(L)+'Time.out', T)
np.savetxt(str(L)+'W.out', W_var)

plt.plot(T, W_var,  'b')
#plt.plot(T_log2,W_log2, 'b')
#plt.plot(T_log3,W_log3, 'b')

#plt.plot(T_log1, intercept1 + slope1*(T_log1), 'r', label=r'$\beta$1 : '+str(slope1))
#plt.plot(T_log2, intercept2 + slope2*(T_log2), 'r', label=r'$\beta$2 : '+str(slope2))
#plt.plot(T_log3, intercept3 + slope3*(T_log3), 'r', label=r'$\beta$3 : '+str(slope3))
plt.legend()
plt.show()


