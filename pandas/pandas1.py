import numpy as np 
import pandas as pd
a=np.arange(9).reshape(3,3)
b=np.linspace(10,18,9).reshape(3,3)
c=a.dot(b)
print(a)
print(b)
print(c.T)
e=pd.Series(range(1,100,23),range(1,100,23))
print(e)
e1=pd.DataFrame(data=a,index=([1,2,3]),columns=(['a','b','c']))
print(e1)