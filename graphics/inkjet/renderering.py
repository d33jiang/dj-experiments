import contextlib
import typing

import cairo
import numpy as np

from inkjet.data import Dot


@contextlib.contextmanager
def child_context(ctx: cairo.Context):
    ctx.save()
    try:
        yield ctx
    finally:
        ctx.restore()


def _draw_dots(
        dots: typing.Sequence[Dot],
        x_lim: typing.Tuple[int, int],
        y_lim: typing.Tuple[int, int],
        output_file_path: str):
    _SCALE_FACTOR = 4

    offsets = (-x_lim[0], -y_lim[0])
    lengths = (x_lim[1] - x_lim[0], y_lim[1] - y_lim[0])

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, _SCALE_FACTOR * lengths[0], _SCALE_FACTOR * lengths[1])
    ctx = cairo.Context(surface)

    with child_context(ctx):
        ctx.scale(_SCALE_FACTOR, _SCALE_FACTOR)
        ctx.translate(*offsets)

        def fill_margin():
            ctx.set_source_rgba(0, 0, 0, 0.5)
            ctx.fill()

        with child_context(ctx):
            # Top margin
            ctx.rectangle(x_lim[0], y_lim[0], lengths[0], -y_lim[0])
            fill_margin()

            # Bottom margin
            ctx.rectangle(x_lim[0], y_lim[1], lengths[0], y_lim[0])
            fill_margin()

            # Left margin
            ctx.rectangle(x_lim[0], y_lim[0], -x_lim[0], lengths[1])
            fill_margin()

            # Right margin
            ctx.rectangle(x_lim[1], y_lim[0], x_lim[0], lengths[1])
            fill_margin()

        ctx.translate(0.5, 0.5)

        # def sketch_dot(x, y, r):
        #     ctx.arc(x, y, r, 0, 2 * np.pi)

        def sketch_dot(x, y, r):
            ctx.rectangle(x - r, y - r, 2 * r, 2 * r)

        def fill_dot(c):
            if len(c) == 4:
                ctx.set_source_rgba(*c)
            else:
                ctx.set_source_rgb(*c)

            ctx.fill()

        with child_context(ctx):
            for dot in dots:
                sketch_dot(dot.x, dot.y, dot.r)
                fill_dot(dot.colour)

    # Write output to file
    surface.write_to_png(output_file_path)


def render_to_file(
        data: np.ndarray,
        dot_rendering_function: typing.Callable[[float, float, np.ndarray], typing.Iterable[Dot]],
        output_file_path: str):
    _MARGIN_SIZE = 12

    dots = []

    h, w = np.shape(data)[0:2]
    for y in range(h):
        for x in range(w):
            dots.extend(dot_rendering_function(x, y, data[y, x, :3]))

    _draw_dots(
        dots=dots,
        x_lim=(-_MARGIN_SIZE, w + _MARGIN_SIZE),
        y_lim=(-_MARGIN_SIZE, h + _MARGIN_SIZE),
        output_file_path=output_file_path
    )
