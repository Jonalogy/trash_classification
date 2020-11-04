import itertools
import numpy as np
import matplotlib.pyplot as plt
from typing import Iterable


def plot_confusion_matrix(confusion_matrix=None, plot_name="Confusion Matrix", class_names: Iterable[str] = None):
    """
    Returns a matplotlib figure containing the plotted confusion matrix.

    Args:
      confusion_matrix (array, shape = [n, n]): a confusion matrix of integer classes
      plot_name (string): a name for the plot
      class_names (array, shape = [n]): String names of the integer classes
    """
    figure = plt.figure(figsize=(8, 8))
    plt.imshow(confusion_matrix, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title(f"{plot_name.strip()} Confusion")
    plt.colorbar()
    tick_marks = np.arange(len(class_names))
    plt.xticks(tick_marks, class_names, rotation=45)
    plt.yticks(tick_marks, class_names)

    # Compute the labels from the normalized confusion matrix.
    # labels = np.around(cm.astype('float') / cm.sum(axis=1)[:, np.newaxis], decimals=2)

    # Use white text if squares are dark; otherwise black.
    threshold = confusion_matrix.max() / 2.
    for i, j in itertools.product(range(confusion_matrix.shape[0]), range(confusion_matrix.shape[1])):
        color = "white" if confusion_matrix[i, j] > threshold else "black"
        plt.text(j, i, confusion_matrix[i, j], horizontalalignment="center", color=color)
        # plt.text(j, i, labels[i, j], horizontalalignment="center", color=color)

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    return figure
