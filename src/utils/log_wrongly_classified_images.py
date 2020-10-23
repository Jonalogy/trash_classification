import numpy as np
import tensorflow as tf


def log_wrongly_classified_images(classnames, wrong_predictions, wrong_images, logdir_path, max_outputs=10):
    """
      classnames = List of class names in strings
      wrong_predictions = list of integers that represent the classes
      images = a numpy array of images in 8-bit integer
      logdir_path = a string for the log directory path
    """
    for class_idx, _ in enumerate(classnames):
        indicies = np.where(wrong_predictions == class_idx)
        total_class_falsies = len(indicies[0])
        wronged_images = np.take(wrong_images, indicies, axis=0)[0]

        # Attempt to write an image summary
        file_writer_cm = tf.summary.create_file_writer(logdir_path)
        with file_writer_cm.as_default():
            tf.summary.image(
                f"Falsely classified as {classnames[class_idx]}",
                wronged_images,
                step=0,
                max_outputs=max_outputs,
                description=f"A total of {total_class_falsies} images wrongly classified as {classnames[class_idx]}. Only a max of {max_outputs} will be shown"
            )
