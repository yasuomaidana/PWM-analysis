import numpy as np
from transformations.Park import inv_park
from transformations.Clarke import inv_clark

pi = np.pi
simulation_time = 3
time_step = 1e-4
ticks = int(simulation_time / time_step)

simulation_time = time_step * ticks
t = np.linspace(0, simulation_time, ticks)

f = 1
w = 2 * pi * f
theta = w * t

Vd = 0
Vq = -1.2
Vo = 0
dq = np.array([[Vd], [Vq], [Vo]])

alpha_beta_gamma = inv_park(theta, dq)
uvw = inv_clark(alpha_beta_gamma)
uvw2 = [inv_clark(abg) for abg in alpha_beta_gamma]
