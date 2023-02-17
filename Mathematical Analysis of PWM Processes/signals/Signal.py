import math

import numpy as np
from scipy import signal


class Signal:
    def __init__(self, amplitude: float = 1, frequency: float = 1, angular_frequency: float = None, offset: float = 0,
                 phi: float = 0):

        self.out = []
        self.t = []

        if angular_frequency is not None:
            frequency = angular_frequency / (2 * math.pi)
            self.angular_frequency = angular_frequency
        else:
            self.angular_frequency = 2 * math.pi * frequency

        self.amplitude = amplitude
        self.frequency = frequency
        self.period = 1 / frequency
        self.offset = offset
        self.fun = lambda x: x
        self.phi = np.deg2rad(phi)

    def output(self, t=None):
        if t is None:
            return self.out
        self.t = t
        self.out = self.fun(t) + self.offset


class SineSignal(Signal):
    def __init__(self, amplitude: float = 1, frequency: float = 1, angular_frequency: float = None, offset: float = 0,
                 phi: float = 0, time: list = None):
        Signal.__init__(self, amplitude, frequency, angular_frequency, offset, phi)
        self.fun = lambda t: self.amplitude * np.sin(self.angular_frequency * t + self.phi)
        if time is not None:
            self.output(time)


class CarrierSignal(Signal):
    def __init__(self, amplitude: float = 1, frequency: float = 1, angular_frequency: float = None, offset: float = 0,
                 width: float = 0.5, phi: float = 0, time: list = None):
        Signal.__init__(self, amplitude, frequency, angular_frequency, offset, phi)
        self.width = width
        self.fun = lambda t: self.amplitude * signal.sawtooth(self.angular_frequency, self.width)

        if time is not None:
            self.output(time)
