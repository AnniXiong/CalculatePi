import numpy as np
import matplotlib.pyplot as plt
import math


Noft = 400  # number of trials
Nofp = 400   # number of points
pi = []      # the list of pi
stdev = []   # list of standard deviations for each different number of trials/points
count = 0
NofTP = []  # list of #of trials/points used every time

while Nofp > 0:
	# here is changing the number of points before nenerating the list of pi values
	NofTP.append(Nofp)
	pi = []
	
	for i in range(Noft):	
	
		count = 0
		for j in range(Nofp):
			x = np.random.uniform(0,1)
			y = np.random.uniform(0,1)
			py = math.sqrt(1 - (x**2))
			if y < py:
				count = count + 1.0
		
		ratio = count/Nofp
		calculatedPi = ratio*4
		pi.append (calculatedPi)
	
	Nofp-=20 # step size
	std = np.std(pi)
	stdev.append(std)

plt.plot(NofTP,stdev,'ro')
plt.xlabel('# of trials')
plt.ylabel('standardDevaition')
plt.title('QualityOfPi')

plt.subplots_adjust(left=0.15)
plt.show()
