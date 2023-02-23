from signals.Signal import SineSignal

from models.Triphasic import Triphasic
import numpy as np
from transformations.Park import park
from transformations.Clarke import clark
import matplotlib.pyplot as plt

def d_polar(theta,vd):
    return np.cos(theta)*vd, np.sin(theta)*vd
def q_polar(theta,vq):
    return -np.sin(theta)*vq, np.cos(theta)*vq


pi = np.pi
simulation_time = 3
time_step = 1e-4
ticks = int(simulation_time / time_step)

simulation_time = time_step * ticks
t = np.linspace(0, simulation_time, ticks)

Vu = SineSignal(time=t)
Vv = SineSignal(phi=-120, time=t)
Vw = SineSignal(phi=+120, time=t)

triphasic_system = Triphasic(time=t)

sys_vu = triphasic_system.Vu
sys_vv = triphasic_system.Vv
sys_vw = triphasic_system.Vw

clark_transformed = clark(np.array([Vu.out, Vv.out, Vw.out]))
sys_clark_transformed = clark(triphasic_system.out)
alpha, beta, gamma = sys_clark_transformed

if not (clark_transformed == sys_clark_transformed).all():
    print("Not well transformed")

theta = Vu.angular_frequency * t

theta2 = np.arctan2(beta, alpha) # + np.pi / 2

vd, vq, vo = park(theta, sys_clark_transformed)
vd2, vq2, vo2 = park(theta2, sys_clark_transformed)

dxy_polar = [d_polar(theta_val,vd_val) for theta_val, vd_val in zip(theta,vd)]
qxy_polar = [q_polar(theta_val,vq_val) for theta_val, vq_val in zip(theta,vq)]

dx, dy = dxy_polar[0]
qx, qy = qxy_polar[0]

fig, axs = plt.subplots(3, figsize=(15, 10))

axs[0].plot(t, Vu.out, t, Vv.out, t, Vw.out)
axs[0].set_xlabel("time[s]")
axs[0].set_ylabel("V")
axs[0].legend(["Vu", "Vv", "Vw"])
# axs[0].set_title("Time domain")

axs[1].plot(t, alpha.flat, t, beta.flat, t, gamma.flat)
axs[1].legend(["Valpha", "Vbeta", "Vgamma"])
axs[1].set_xlabel("time[s]")
axs[1].set_ylabel("V")
# axs[1].set_title("Alpha beta gamma axis reference")

axs[2].plot(t, vd, t, vq, t, vo, "r--")
axs[2].legend(["Vd", "Vq", "Vo"])
axs[2].set_xlabel("time[s]")
axs[2].set_ylabel("V")
# axs[2].set_title("Alpha beta gamma axis reference")

plt.show()
