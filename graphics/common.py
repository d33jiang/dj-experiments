import matplotlib.pyplot as plt
import numpy as np


def show_bitmap(data: np.ndarray, title: str):
    plt.imshow(np.clip(data, a_min=0, a_max=255), cmap='gray')
    plt.axis('off')
    plt.title(title)
    plt.show()
