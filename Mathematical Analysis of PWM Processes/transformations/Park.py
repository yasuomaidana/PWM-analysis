import numpy as np
from numpy import linalg

phi = np.pi * 2 / 3


def park_matrix(theta: float) -> np.array:
    return np.sqrt(2 / 3) * np.array([[np.sin(theta), np.sin(theta - phi), np.sin(theta + phi)],
                                      [np.cos(theta), np.cos(theta - phi), np.cos(theta + phi)],
                                      np.sqrt(1 / 2) * np.ones(3)])


def inv_park_matrix(theta: float) -> np.array:
    return linalg.inv(park_matrix(theta))


def park(theta: float, alpha_beta_gamma: np.array) -> np.array:
    if not isinstance(theta, float):
        return np.array([np.matmul(park_matrix(theta_i), alpha_beta_gamma[:, i]) for i, theta_i in enumerate(theta)]) \
            .transpose()
    return np.matmul(park_matrix(theta), alpha_beta_gamma)
