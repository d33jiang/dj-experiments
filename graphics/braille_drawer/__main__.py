import numpy as np

import image_provider
from braille_drawer.renderer import render_to_string
from common import show_bitmap

#
# Reference Image

img_working = image_provider.img_reference

show_bitmap(img_working, 'Reference')

print('Threshold on Red Signal in Reference Image\n')
print(render_to_string(img_working[:, :, 0] >= 128))

#
# Images with Transparency

img_working = image_provider.img_tree

show_bitmap(img_working, 'Tree')

img_working = np.logical_and(
    np.mean(img_working[:, :, 0:3], axis=2) < 128,
    img_working[:, :, 3] >= 128
)

print('\n\nThreshold on Average RGB Signal and Alpha Signal in Tree Image\n')
print(render_to_string(img_working))
