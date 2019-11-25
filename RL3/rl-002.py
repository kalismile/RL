import tensorflow as tf  
import numpy as np  
import gym



env=gym.make('CartPole-v0')
env.reset()
print(env.metadata)
for i in range(1000):
    env.step(env.action_space.sample())
    env.render()
env.close()

a1=np.arange(1,10).reshape(3,3)
a2=np.arange(10,19).reshape(3,3)
b1=tf.constant(a1)
b2=tf.constant(a2)
print(tf.matmul(b1,b2))