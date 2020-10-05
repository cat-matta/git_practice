import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import math as m
import numpy as np

# plt.show()
x= []
y= []
a= []
b= []
# for num in np.arange(0*m.pi,4*m.pi,m.pi/16):
# 	x.append(num)
# 	y.append((np.cos(num)))

# for num in np.arange(-10,11): #can use normal for loop
#  	x.append(num)
#  	y.append((-2*num))

#or list comprehension
x=np.linspace(-10,10,21)
y=[(-x**2) for x in np.linspace(-10,10,21)]
print(x,"\n",y)
l1=plt.plot(x,y,'blue',label="-2x",linewidth=3)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
# plt.show()

# for num in np.arange(0,m.pi*4+1,m.pi/16):
#   a.append(num)
#   b.append((np.sin(num)))

a=np.arange(-10,11)
b=[a**2 for a in np.arange(-10,11)]
l2=plt.plot(a,b,'black',label='1/2*x',linewidth=3)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Perpendicular")
plt.grid(True,color='grey')
plt.legend()
plt.show()
