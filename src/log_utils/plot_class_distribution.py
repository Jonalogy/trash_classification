from io import BytesIO
import matplotlib.pyplot as plt
from typing import List
import numpy as np


def _autolabel(ax, rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


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

    fig, ax = plt.subplots()
    plt.xticks(rotation=45)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Images count')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(x_pos + bar_width)
    ax.set_xticklabels(classes)
    ax.legend()
    # set rotation to 45 degrees

    bars = []
    for (color, label, distro) in list_distro:
        bars.append(
            ax.bar(x=x_pos, width=bar_width, height=distro, color=color, label=label)
        )
        x_pos = x_pos + bar_width

    [_autolabel(ax, bar) for bar in bars]

    buffer = BytesIO()

    y_max = np.amax([*train_distro, *valid_distro, *test_distro])
    plt.ylim(top=y_max + 3) # To add space between the bar annotations and the top of the plot

    plt.savefig(buffer, format='png')
    plt.close()
    return buffer
