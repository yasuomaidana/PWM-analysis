import math

import numpy as np
from numpy import linalg

phi = np.pi * 2 / 3


def park_matrix(theta: float) -> np.matrix:
    return 2 / 3 * np.matrix([[np.sin(theta), np.sin(theta - phi), np.sin(theta + phi)],
                              [np.cos(theta), np.cos(theta - phi), np.cos(theta + phi)],
                              1 / 2 * np.ones(3)])


def inv_park_matrix(theta: float) -> np.matrix:
    return linalg.inv(park_matrix(theta))
