from __future__ import print_function, division
import tensorflow as tf
from hello_world_not_main import not_main_print

hello_world = tf.constant('Hello world!')

with tf.Session() as sess:
    print(sess.run(hello_world))

not_main_print()
