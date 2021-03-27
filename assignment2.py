import array as arr
import numpy as np
import matplotlib.pyplot as plt
import math
# we construct a function for combination
def comb(n,r):
  return math.factorial(n)/(math.factorial(n-r)*math.factorial(r))
y1=arr.array('f',[]) #here y1 is the array of simulation results
y=arr.array('f',[])  #here y is the array of theoretical results
x=arr.array('f',[]) #x is the array of input values of 2n (the total number of coin tosses)
for k in range(1,10):
  y.append(comb(2*k,k)/(4**k))
  x.append(2*k)
  total_cases=0 #this is the total number of 2k coin tosses required for simulation
  favourable_cases=0 #this is the number of 2k coin tosses in which k heads are obtained.
  for a in range (1,5000): #here we toss 2k coins 5000 times for simulating result
     trial=np.random.binomial(n=1,p=0.5,size=2*k)
     total_cases+=1
     if (list(trial).count(1)==k):
       favourable_cases+=1 
  y1.append(favourable_cases/total_cases)#we append the simulation value of probability to y1
w=0.5 #width
x1=[a+w for a in x]
plt.bar(x,y,w,label='theoretical value')
plt.bar(x1,y1,w,label='simulation value')
plt.xlabel("total number of tosses=2n")
plt.ylabel("probability of getting n heads")
plt.title("Theoretical value vs simulation value")
plt.xticks(np.arange(0,20,1))
plt.yticks(np.arange(0,1,0.05))
plt.legend()
plt.show()
print("As we can see from the graph, the theoretical values and simulation values are approximately equal")