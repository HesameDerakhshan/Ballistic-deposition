
from random import randrange
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import math

l          = 128 # l -> L
W_var = []
T         = []
t          = 100000000
j          = 1
step    = 0
h         = np.zeros(l)

L     =range(0,l)
T_log1 = []
W_log1 = []
T_log2 = []
W_log2 = []
T_log3 = []
W_log3 = []


while (j<t):
    
	i = randrange(l)
	h[i%l] = max(1 + h[i%l], h[(i-1)%l], h[(i+1)%l])

	W_var.append(np.var(h))
	T.append(j)
	
	#logaritmic increase while loop step
	j=j+1


#log of W_var and T array
for i in range(len(T)):
	ti = math.log10(T[i])
	wi = math.log10(W_var[i])
	if (ti<=9):
		T_log1.append(ti)
		W_log1.append(wi)
	elif (ti<=5.11):
		T_log2.append(ti)
		W_log2.append(wi)
	elif(ti> 5.11):
		T_log3.append(ti)
		W_log3.append(wi)
		
		
#conver list to array	
T_log1 = np.asarray(T_log1)
W_log1 = np.asarray(W_log1)
T_log2 = np.asarray(T_log2)
W_log2 = np.asarray(W_log2)
T_log3 = np.asarray(T_log3)
W_log3 = np.asarray(W_log3)

		
#linre curve fiting function 	
#slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(T_log1,W_log1)
#slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(T_log2, W_log2)
#slope3, intercept3, r_value3, p_value3, std_err3 = stats.linregress(T_log3, W_log3)


#print("beta1: ",slope1,"beta2: ",slope2,"beta3: ",slope3)

plt.plot(T_log1,W_log1, 'b')
plt.plot(T_log2,W_log2, 'b')
plt.plot(T_log3,W_log3, 'b')

#plt.plot(T_log1, intercept1 + slope1*(T_log1), 'r', label=r'$\beta$1 : '+str(slope1))
#plt.plot(T_log2, intercept2 + slope2*(T_log2), 'r', label=r'$\beta$2 : '+str(slope2))
#plt.plot(T_log3, intercept3 + slope3*(T_log3), 'r', label=r'$\beta$3 : '+str(slope3))
plt.legend()
plt.show()


