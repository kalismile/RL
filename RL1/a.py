import tensorflow as tf 
a=tf.constant([3,4])
b=tf.constant([6,3])
result=a+b
sess=tf.Session()
print(sess.run(result))