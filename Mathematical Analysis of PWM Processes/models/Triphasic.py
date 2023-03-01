import numpy as np
from .signals.Signal import SineSignal


class Triphasic:
    def __init__(self, amplitude: float = 1, frequency: float = 1, time: list = None):
        self.Vu = SineSignal(amplitude, frequency, time=time)
        self.Vv = SineSignal(amplitude, frequency, phi=-120, time=time)
        self.Vw = SineSignal(amplitude, frequency, phi=+120, time=time)
        self.t = time
        self.out = np.array([self.Vu.out, self.Vv.out, self.Vw.out])
        
    def output(self, t=None) -> np.array:
        if t is None:
            return self.out
        self.t = t
        self.out = np.array([self.Vu.output(t), self.Vv.output(t), self.Vw.output(t)])
        return self.out
