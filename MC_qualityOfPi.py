import numpy as np
import matplotlib.pyplot as plt
import math


Noft = 4000
Nofp = 200
pi = []
stdev = []
count = 0
NofTP = []

while Noft > 0:
	NofTP.append(Noft)
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
	
	#print(pi)
	Noft-=20
	std = np.std(pi)
	stdev.append(std)

'''print(NofTrial)
print(stdev)
print(len(NofTrial),len(stdev))
'''
plt.plot(NofTP,stdev,'ro')
plt.xlabel('# of trials')
plt.ylabel('standardDevaition')
plt.title('QualityOfPi')

plt.subplots_adjust(left=0.15)
plt.show()