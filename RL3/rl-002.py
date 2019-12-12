
import tensorflow as tf  
import numpy as np  
import gym
import os 

tf.test.gpu_device_name()
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
print('GPU is there',tf.test.is_gpu_available())
print('\r\n\r\n\r\n888888888888888888888888=')

# env=gym.make('CartPole-v0')
# env.reset()
# print(env.metadata)
# for i in range(1000):
#     env.step(env.action_space.sample())
#     env.render()
# env.close()

a1=np.arange(1,10).reshape(3,3)
a2=np.arange(10,19).reshape(3,3)
b1=tf.constant(a1)
b2=tf.constant(a2)
for i in range(1):
    e=tf.matmul(b1,b2)

import timeit

with tf.device('/cpu:0'):
   cpu_a = tf.random.normal([10000, 1000])
   cpu_b = tf.random.normal([1000, 2000])
   print(cpu_a.device, cpu_b.device)

with tf.device('/gpu:0'):
   gpu_a = tf.random.normal([10000, 1000])
   gpu_b = tf.random.normal([1000, 2000])
   print(gpu_a.device, gpu_b.device)

def cpu_run():
   with tf.device('/cpu:0'):
      c = tf.matmul(cpu_a, cpu_b)
   return c

def gpu_run():
   with tf.device('/gpu:0'):
      c = tf.matmul(gpu_a, gpu_b)
   return c

cpu_time = timeit.timeit(cpu_run, number=1000)
gpu_time = timeit.timeit(gpu_run, number=1000)
print('warmup:', cpu_time, gpu_time)

cpu_time = timeit.timeit(cpu_run, number=1000)
gpu_time = timeit.timeit(gpu_run, number=1000)
print('run time:', cpu_time, gpu_time)