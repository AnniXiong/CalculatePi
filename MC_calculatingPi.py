import numpy as np
import matplotlib.pyplot as plt
import math

NofEvent = 1000
pi = []
count = 0

for i in range(NofEvent):	
	
	count = 0
	for j in range(NofEvent):
		x = np.random.uniform(0,1)
		y = np.random.uniform(0,1)
		py = math.sqrt(1 - (x**2))
		if y < py:
			count = count + 1.0
		
	ratio = count/NofEvent
	calculatedPi = ratio*4
	pi.append (calculatedPi)
    
	
num_bins = 50
n, bins, patches = plt.hist(pi, num_bins,normed=1, facecolor='blue', alpha=0.5)

plt.xlabel('result')
plt.ylabel('Probability')
plt.title('Calculating pi')

plt.subplots_adjust(left=0.15)
plt.show()























