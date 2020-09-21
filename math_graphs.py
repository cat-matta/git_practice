import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import math as m
import numpy as np


# f,ax=plt.subplots(figsize=(20,10))
# x=np.linspace(0, 10*np.pi,1000)
# y=np.sin(x)

# ax.plot(x/np.pi,y)

# ax.xaxis.set_major_formatter(tck.FormatStrFormatter('%g $\pi$'))
# ax.xaxis.set_major_locator(tck.MultipleLocator(base=1.0))

# plt.style.use("ggplot")


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
x=[x for x in np.arange(-10,11)]
y=[(-2*x +4) for x in np.arange(-10,11)]
print(x,"\n",y)
l1=plt.plot(x,y,'blue',label="-2x",linewidth=3)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
# plt.show()

# for num in np.arange(0,m.pi*4+1,m.pi/16):
#   a.append(num)
#   b.append((np.sin(num)))
for num in np.arange(-10,11):
 	a.append(num)
 	b.append(((1/2)*num-3))

l2=plt.plot(a,b,'black',label='1/2*x',linewidth=3)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Perpendicular")
plt.grid(True,color='grey')
plt.legend()
plt.show()
