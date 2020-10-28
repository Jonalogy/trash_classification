import tensorflow as tf


def argmax_int(one_hot_list):
    return tf.math.argmax(one_hot_list, axis=1, output_type=tf.int32)
