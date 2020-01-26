import dataclasses
import typing

import numpy as np


@dataclasses.dataclass
class TileShape:
    name: str
    shape: typing.Tuple[int, int]
    encode_function: typing.Callable[[np.ndarray], int]

    def get_zeros(self):
        return np.zeros(shape=self.shape, dtype=np.uint8)


def _encode_h3w2(tile):
    code = np.sum(np.ravel(tile, 'F') * [1, 2, 4, 8, 16, 32])
    code_point = 0x2800 + code
    return code_point


H3W2 = TileShape(
    'H3W2',
    (3, 2),
    _encode_h3w2
)


def _get_tile_slice(row, col, shape):
    return (
        slice(row * shape[0], (row + 1) * shape[0]),
        slice(col * shape[1], (col + 1) * shape[1])
    )


def _render_block(
        data_block: np.ndarray,
        tile_shape: TileShape):
    if np.shape(data_block) != tile_shape.shape:
        data_block = np.copy(data_block)
        data_block.resize(tile_shape.shape)

    code_point = tile_shape.encode_function(data_block)
    return chr(code_point)


def _render_character_grid(data: np.ndarray, tile_shape: TileShape):
    h, w = np.shape(data)

    shape = np.array([h, w])
    shape = (shape - 1) // tile_shape.shape + 1
    tiles_h, tiles_w = shape

    result = np.zeros(shape=shape, dtype=np.unicode)

    for row in range(tiles_h):
        for col in range(tiles_w):
            tile = data[_get_tile_slice(row, col, tile_shape.shape)]
            result[row, col] = _render_block(tile, tile_shape)

    return result


def render_to_string(data: np.ndarray, tile_shape: TileShape = H3W2):
    grid = _render_character_grid(data, tile_shape)
    return '\n'.join(
        ''.join(grid_row)
        for grid_row in grid
    )
