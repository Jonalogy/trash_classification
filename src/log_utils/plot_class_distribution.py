from io import BytesIO
import matplotlib.pyplot as plt
from typing import List
import numpy as np


def plot_class_distribution(
        classes: List[str],
        train_distro: List[int],
        valid_distro: List[int],
        test_distro: List[int]):
    """
    Returns a file object of matplotlib plot

    Args:
      classes (array, shape = [str]): An iterable containing strings of class names
      train_distro (array): Training dataset's distribution
      valid_distro (array): Validation dataset's distribution
      test_distro (array): Test dataset's distribution
    """

    if len(train_distro) != len(valid_distro) or len(valid_distro) != len(test_distro):
        raise ValueError('Distributions have different lengths!')

    x_pos = np.array([i for i, _ in enumerate(classes)])
    bar_width = 0.25
    list_distro = [
        ('green', 'train', train_distro),
        ('blue', 'validation', valid_distro),
        ('red', 'test', test_distro)
    ]

    plt.xlabel("Class names")
    plt.ylabel("Images count")
    plt.title("Class distribution")
    plt.xticks(ticks=(x_pos + 0.25), labels=classes, rotation=45)

    for (color, label, distro) in list_distro:
        plt.bar(x=x_pos, width=bar_width, height=distro, color=color, label=label)
        x_pos = x_pos + bar_width

    plt.legend()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    return buffer
