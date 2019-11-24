import numpy as np 
a=np.arange(9).reshape(3,3)
b=np.linspace(10,18,9).reshape(3,3)
c=a.dot(b)
print(a)
print(b)
print(c.T)
