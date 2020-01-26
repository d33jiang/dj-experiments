import typing

import numpy as np

from inkjet.data import Dot


def render_pixel_simple(x: float, y: float, channels: np.ndarray) -> typing.Sequence[Dot]:
    _DOT_SIZE = 0.5

    signals = channels / 255
    sig_r, sig_g, sig_b = signals

    return [
        Dot(x, y, _DOT_SIZE, np.array((sig_r, sig_g, sig_b, 1)))
    ]


def render_pixel_rgb_green(x: float, y: float, channels: np.ndarray) -> typing.Sequence[Dot]:
    _DOT_SPREAD = 0.25
    _DOT_SIZE = 0.25

    signals = channels / 255
    sig_r, sig_g, sig_b = signals

    return [
        Dot(x - _DOT_SPREAD, y - _DOT_SPREAD, _DOT_SIZE, np.array((0, sig_g, 0, 1))),
        Dot(x + _DOT_SPREAD, y - _DOT_SPREAD, _DOT_SIZE, np.array((sig_r, 0, 0, 1))),
        Dot(x - _DOT_SPREAD, y + _DOT_SPREAD, _DOT_SIZE, np.array((0, 0, sig_b, 1))),
        Dot(x + _DOT_SPREAD, y + _DOT_SPREAD, _DOT_SIZE, np.array((0, sig_g, 0, 1))),
    ]


def render_pixel_rgb_level(x: float, y: float, channels: np.ndarray) -> typing.Sequence[Dot]:
    _DOT_SPREAD = 0.25
    _DOT_SIZE = 0.25

    sig_r, sig_g, sig_b = channels / 255
    sig_avg = np.mean(channels[0:3]) / 255

    return [
        Dot(x - _DOT_SPREAD, y - _DOT_SPREAD, _DOT_SIZE, np.array((0, sig_g, 0, 1))),
        Dot(x + _DOT_SPREAD, y - _DOT_SPREAD, _DOT_SIZE, np.array((sig_r, 0, 0, 1))),
        Dot(x - _DOT_SPREAD, y + _DOT_SPREAD, _DOT_SIZE, np.array((0, 0, sig_b, 1))),
        Dot(x + _DOT_SPREAD, y + _DOT_SPREAD, _DOT_SIZE, np.array((sig_avg, sig_avg, sig_avg, 1))),
    ]


def render_pixel_rgb_black(x: float, y: float, channels: np.ndarray) -> typing.Sequence[Dot]:
    _DOT_SPREAD = 0.25
    _DOT_SIZE = 0.25

    sig_r, sig_g, sig_b = channels / 255

    return [
        Dot(x - _DOT_SPREAD, y - _DOT_SPREAD, _DOT_SIZE, np.array((0, sig_g, 0, 1))),
        Dot(x + _DOT_SPREAD, y - _DOT_SPREAD, _DOT_SIZE, np.array((sig_r, 0, 0, 1))),
        Dot(x - _DOT_SPREAD, y + _DOT_SPREAD, _DOT_SIZE, np.array((0, 0, sig_b, 1))),
        Dot(x + _DOT_SPREAD, y + _DOT_SPREAD, _DOT_SIZE, np.array((0, 0, 0, 1))),
    ]


def render_pixel_rgb_reference(x: float, y: float, channels: np.ndarray) -> typing.Sequence[Dot]:
    _DOT_SPREAD = 0.25
    _DOT_SIZE = 0.25

    sig_r, sig_g, sig_b = channels / 255

    return [
        Dot(x - _DOT_SPREAD, y - _DOT_SPREAD, _DOT_SIZE, np.array((0, sig_g, 0, 1))),
        Dot(x + _DOT_SPREAD, y - _DOT_SPREAD, _DOT_SIZE, np.array((sig_r, 0, 0, 1))),
        Dot(x - _DOT_SPREAD, y + _DOT_SPREAD, _DOT_SIZE, np.array((0, 0, sig_b, 1))),
        Dot(x + _DOT_SPREAD, y + _DOT_SPREAD, _DOT_SIZE, np.array((sig_r, sig_g, sig_b, 1))),
    ]


def render_pixel_cymk_old(x: float, y: float, channels: np.ndarray) -> typing.Sequence[Dot]:
    _DOT_SPREAD = 0.25
    _DOT_SIZE = 0.25

    signals = channels / 255
    signals = ((1 - signals) + np.roll(signals, 1) + np.roll(signals, 2)) / 3

    inv_signals = 1 - (signals ** 2)
    inv_sig_c, inv_sig_m, inv_sig_y = inv_signals

    sig_cmy_min = np.min(signals)
    sig_k = sig_cmy_min
    sig_w = 1 - sig_k ** 2

    return [
        Dot(x - _DOT_SPREAD, y - _DOT_SPREAD, _DOT_SIZE, np.array((1, inv_sig_m, 1, 1))),
        Dot(x + _DOT_SPREAD, y - _DOT_SPREAD, _DOT_SIZE, np.array((inv_sig_c, 1, 1, 1))),
        Dot(x - _DOT_SPREAD, y + _DOT_SPREAD, _DOT_SIZE, np.array((1, 1, inv_sig_y, 1))),
        Dot(x + _DOT_SPREAD, y + _DOT_SPREAD, _DOT_SIZE, np.array((sig_w, sig_w, sig_w, 1))),
    ]


def render_pixel_cymk_alpha_old(x: float, y: float, channels: np.ndarray) -> typing.Sequence[Dot]:
    _DOT_SPREAD = 0.25
    _DOT_SIZE = 0.25

    signals = channels / 255
    signals = ((1 - signals) + np.roll(signals, 1) + np.roll(signals, 2)) / 3

    signals = signals ** 2
    sig_c, sig_m, sig_y = signals

    sig_k = np.min(signals)
    sig_k = sig_k ** 2

    return [
        Dot(x - _DOT_SPREAD, y - _DOT_SPREAD, _DOT_SIZE, np.array((1, 0, 1, sig_m))),
        Dot(x + _DOT_SPREAD, y - _DOT_SPREAD, _DOT_SIZE, np.array((0, 1, 1, sig_c))),
        Dot(x - _DOT_SPREAD, y + _DOT_SPREAD, _DOT_SIZE, np.array((1, 1, 0, sig_y))),
        Dot(x + _DOT_SPREAD, y + _DOT_SPREAD, _DOT_SIZE, np.array((0, 0, 0, sig_k))),
    ]


def render_pixel_rgb_merge(x: float, y: float, channels: np.ndarray) -> typing.Sequence[Dot]:
    _DOT_SPREAD = 0.25
    _DOT_SIZE = 0.25

    signals = channels / 255
    sig_r, sig_g, sig_b = signals

    sig_w = np.mean(signals)

    return [
        Dot(x - _DOT_SPREAD, y - _DOT_SPREAD, _DOT_SIZE, np.array((sig_r, 0, sig_b, 1))),
        Dot(x + _DOT_SPREAD, y - _DOT_SPREAD, _DOT_SIZE, np.array((0, sig_g, sig_b, 1))),
        Dot(x - _DOT_SPREAD, y + _DOT_SPREAD, _DOT_SIZE, np.array((sig_r, sig_g, 0, 1))),
        Dot(x + _DOT_SPREAD, y + _DOT_SPREAD, _DOT_SIZE, np.array((sig_w, sig_w, sig_w, 1))),
    ]


def render_pixel_cymk(x: float, y: float, channels: np.ndarray) -> typing.Sequence[Dot]:
    _DOT_SPREAD = 0.25
    _DOT_SIZE = 0.25

    signals = channels / 255
    signals = 1 - signals
    sig_c, sig_m, sig_y = signals

    sig_k = np.min(signals)
    # sig_k = sig_k ** 2

    return [
        Dot(x - _DOT_SPREAD, y - _DOT_SPREAD, _DOT_SIZE, np.array((1, 0, 1, sig_m))),
        Dot(x + _DOT_SPREAD, y - _DOT_SPREAD, _DOT_SIZE, np.array((0, 1, 1, sig_c))),
        Dot(x - _DOT_SPREAD, y + _DOT_SPREAD, _DOT_SIZE, np.array((1, 1, 0, sig_y))),
        Dot(x + _DOT_SPREAD, y + _DOT_SPREAD, _DOT_SIZE, np.array((0, 0, 0, sig_k))),
    ]
