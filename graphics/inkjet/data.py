import dataclasses
import typing


@dataclasses.dataclass
class Dot:
    x: float
    y: float
    r: float
    colour: typing.Any
