from typing import Callable, Any, Union

from numpy import sin, cos, radians

m: Callable[[float, float], float] = lambda v_sr, v_dc: v_sr * 3 / (2 * v_dc)


def time_calculator(modulation_factor: float, alpha: float, Ts: float) -> [float, float, float]:
    t1 = modulation_factor * sin(radians(60 - alpha)) / sin(radians(60))
    t2 = modulation_factor * sin(radians(alpha)) / sin(radians(60))
    to = Ts - t1 - t2
    return t1, t2, to
