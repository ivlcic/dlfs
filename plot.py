import matplotlib.pyplot as plt
from numpy import ndarray
from typing import List


def plot_single(list_of_ranges: List[ndarray], titles: List[str]):
    num_g = len(titles)
    assert len(list_of_ranges) == 2 * num_g

    fig, ax = plt.subplots(1, num_g, sharey='none', figsize=(num_g * 6, 6))
    for i, title in enumerate(titles):
        ax[i].plot(list_of_ranges[i * 2], list_of_ranges[(i * 2) + 1])
        # ax[0].plot(input_range, square(input_range))
        ax[i].set_title(title)
        ax[i].set_xlabel('input')
        ax[i].set_ylabel('output')
        ax[i].grid(True)
        ax[i].axis('scaled')
    plt.show()
