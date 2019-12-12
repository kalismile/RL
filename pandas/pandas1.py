# # -*- coding:utf-8-*-
# import numpy as np 
# import pandas as pd
# # import scipy
# # # import seaborn as sns
# # import matplotlib.pyplot as plt 
# # import statsmodels as sm  
# import tensorflow as tf
 




# # a=np.arange(9).reshape(3,3)
# # b=np.linspace(10,18,9).reshape(3,3)
# # c=a.dot(b)
# # print(a)
# # print(b)
# # print(c.T)
# # e=pd.Series(range(1,100,23),range(1,100,23))
# # print(e)
# # e1=pd.DataFrame(data=a,index=([1,2,3]),columns=(['a','b','c']))
# # print(e1)
# # class liu():
# #     a=5
# #     b=6
# #     def cc(c):
# #         c=c
# #         print(c) 

# # liu.cc(50)
# # liu.a=5000
# # print(liu.a)
# # ming=liu

# # ming.cc(100)
# # print(ming.a) 
# # a = ['Mary', 'had', 'a', 'little', 'lamb']
# # print(range(10))

# a=[3,4,5,'abc']
# print(len(a))

# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')
# for b in range(5):
#     for a in range(4):
#         print(b,'  one   ',a)
# # else:
#     print(b,'  two  ' ,a)
# def fib(n):
#     a=0
#     b=1
#     while a<n:
#         a,b=b,a+b
#         print(a,'\r')
# fib(50)
# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.")
#     print("-- Lovely plumage, the", type)
#     print("-- It's", state, "!")
# parrot(1000)

# def f(*args,a='-'):
#     return a.join(*args)
# print(f(['sdf','324','njh']))

# def parrot(voltage, state='a stiff', action='voom'):
#     print('*'*40)
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.", end=' ')
#     print("E's", state, "!")

# d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
# parrot(**d)
# def f(n):
#     return lambda a:a**n

# f1=f(4)
# print(f1(2))
