import math

import numpy as np
from numpy import linalg

# Here we calculate the POWER invariant transformation
clarke_matrix = np.matrix(
    [[1, -1 / 2, -1 / 2], [0, math.sqrt(3) / 2, -math.sqrt(3) / 2], 1.0 / math.sqrt(2) * np.ones(3)])
inverse_clarke_matrix = linalg.inv(clarke_matrix)


def clark(input_signal: np.matrix) -> np.matrix:
    return clarke_matrix * input_signal


def inv_clark(input_signal: np.matrix) -> np.matrix:
    return inverse_clarke_matrix * input_signal
