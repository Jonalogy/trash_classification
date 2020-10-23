import tensorflow as tf
from .argmax_int import argmax_int


def extract_truth_and_predictions(model, tf_dataset):
    labels = tf.constant([], dtype=tf.int32)  # setting to 8 bits since there are only 5 material classes
    predictions = tf.constant([], dtype=tf.int32)  # setting to 8 bits since there are only 5 material classes

    for (images, classes) in tf_dataset:
        labels = tf.concat((labels, argmax_int(classes)), axis=0)
        y_hat = argmax_int(model.predict(x=images))
        predictions = tf.concat((predictions, y_hat), axis=0)

    return labels, predictions
