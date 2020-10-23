import tensorflow as tf
import numpy as np
from .argmax_int import argmax_int


def extract_truth_and_predictions(model, tf_dataset):
    truth = tf.constant([], dtype=tf.int32)  # setting to 8 bits since there are only 5 material classes
    predictions = tf.constant([], dtype=tf.int32)  # setting to 8 bits since there are only 5 material classes
    wrongly_classified_images = None
    wrong_predictions = None

    for (images, classes) in tf_dataset:
        truth_classes = argmax_int(classes)
        y_hats = argmax_int(model.predict(x=images))

        index_false_prediction = np.where(tf.math.equal(truth_classes, y_hats) == False)[0]
        failed_images = np.take(images.numpy(), index_false_prediction, axis=0)
        wrong_yhats = np.take(y_hats, index_false_prediction, axis=0)

        if None.__class__ == type(wrongly_classified_images):
            wrongly_classified_images = failed_images
            wrong_predictions = wrong_yhats
        else:
            wrongly_classified_images = np.concatenate(
                [wrongly_classified_images, failed_images],
                axis=0
            )
            wrong_predictions = np.concatenate(
                [wrong_predictions, wrong_yhats],
                axis=0
            )

        truth = tf.concat((truth, truth_classes), axis=0)
        predictions = tf.concat((predictions, y_hats), axis=0)

    return truth, predictions, (wrongly_classified_images, wrong_predictions)
