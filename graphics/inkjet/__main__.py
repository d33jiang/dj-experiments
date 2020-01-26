import matplotlib.pyplot as plt

import image_provider
from common import show_bitmap
from inkjet import dot_renderers
from inkjet.renderering import render_to_file

img_reference = image_provider.img_morning_sky

if True:
    dot_rendering_functions = {
        # Pixel is True Colour (Normal Rendering)
        dot_renderers.render_pixel_simple: '0_normal',
        # Last Dot is Green Signal (Old TV Style)
        dot_renderers.render_pixel_rgb_green: '1_green',
        # Last Dot is Mean Signal (Truer Brightness)
        dot_renderers.render_pixel_rgb_level: '2_level',
        # Last Dot is Black (Truer Colour)
        dot_renderers.render_pixel_rgb_black: '3_black',
        # Last Dot is True Colour
        dot_renderers.render_pixel_rgb_reference: '4_reference',
        # Dots are Mixes of RGB Signal
        dot_renderers.render_pixel_rgb_merge: '5_merge',
        # Attempt at CYMK
        dot_renderers.render_pixel_cymk: '6_cymk',
    }

    for func, label in dot_rendering_functions.items():
        output_file_path = f'resources/output/inkjet/{label}.png'

        # Render to file
        render_to_file(img_reference, func, output_file_path)

        # Display output from file
        img_output = plt.imread(output_file_path)
        show_bitmap(img_output, 'Output')
