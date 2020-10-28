import os
from pathlib import Path
from typing import List
import tensorflow as tf
from src.log_utils import extract_truth_and_predictions, plot_confusion_matrix, log_confusion_matrix, \
    log_wrongly_classified_images


def evaluate_model(
        model: tf.keras.Model,
        test_ds, class_names: List[str],
        log_dir: str,
        training_tag: str,
        cm_name: str,
        log_false_images=False):
    model.evaluate(x=test_ds)
    (
        labels, predictions,
        (wrongly_classified_images, wrong_predictions)
    ) = extract_truth_and_predictions(model, test_ds)

    cm_figure = plot_confusion_matrix(
        cm=tf.math.confusion_matrix(labels, predictions).numpy(),
        class_names=class_names
    )

    logdir = str(log_dir) if isinstance(log_dir, Path) else log_dir

    log_confusion_matrix(os.path.join(logdir, 'cm', training_tag), cm_name, cm_figure)

    if log_false_images:
        log_wrongly_classified_images(
            classnames=class_names,
            wrong_predictions=wrong_predictions,
            wrong_images=wrongly_classified_images.astype('uint8'),
            logdir_path=os.path.join(log_dir, 'images', training_tag)
        )
