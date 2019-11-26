
import tensorflow as tf  
import numpy as np  
import gym
import os 
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0'
tf.test.gpu_device_name()
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
print('GPU is there',tf.test.is_gpu_available())

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

