import matplotlib.pyplot as plt
import numpy as np


def _float_to_uint8(data: np.ndarray):
    return np.uint8(255 * data)


def _import_png(file_path: str):
    img = plt.imread(file_path)
    img = _float_to_uint8(img)
    return img


def _import_jpeg(file_path: str):
    img = plt.imread(file_path)
    img = -img
    img = _float_to_uint8(img)
    return img


def _downscale_image(img: np.ndarray, factor: int):
    from skimage.transform import resize

    img = resize(
        img,
        (img.shape[0] // factor, img.shape[1] // factor),
        anti_aliasing=True
    )

    img = _float_to_uint8(img)
    return img


def _save_image(img: np.ndarray, file_path: str):
    plt.imsave(file_path, img)


img_reference = _import_png('resources/reference.png')
img_northern_lights = _import_png('resources/downscaled_northern_lights.png')
img_tree = _import_png('resources/downscaled_tree.png')
img_morning_sky = _import_png('resources/downscaled_morning_sky.png')
