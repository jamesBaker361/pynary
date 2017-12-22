import tensorflow as tf

x_arr=[]
y_arr=[]

x_arr=raw_input("x values?")
y_arr=raw_input("y values?")

sess = tf.Session()

w = tf.Variable([.5], tf.float32)
b = tf.Variable([-.5], tf.float32)
x = tf.placeholder(tf.float32)

linear_model = w * x + b

init = tf.global_variables_initializer()
sess.run(init)

print(sess.run(linear_model, {x:[1,2,3,4]}))

y = tf.placeholder(tf.float32)
squared_deltas = tf.square(linear_model-y)
less = tf.reduce_sum(squared_deltas)
print(sess.run(less,{x:[2,3],y:[6,5]}))

sess.run(init)

optimizer=tf.train.GradientDescentOptimizer(0.1)
train=optimizer.minimize(less)

for i in range(1000):
    sess.run(train, {x:x_arr, y:y_arr})
print(sess.run([w,b]))