import numpy as np
from signals.Signal import CarrierSignal, SineSignal
import matplotlib.pyplot as plt
from transformations.sampling import natural_sampling, asymmetrical_sampling, symmetrical_sampling

pi = np.pi

simulation_time = 1
time_step = 1e-5
ticks = int(simulation_time / time_step)
simulation_time = time_step * ticks
t = np.linspace(0, simulation_time, ticks)

fs = 1
m = 0.8

modulated = SineSignal(amplitude=m, frequency=fs, time=t)
carrier = CarrierSignal(angular_frequency=21 * modulated.angular_frequency, time=t)

natural_sampled = natural_sampling(carrier, modulated)
asymmetrically_modulated, asymmetrically_sampled = asymmetrical_sampling(carrier, modulated)
symmetrically_modulated, symmetrically_sampled = symmetrical_sampling(carrier, modulated)

fig, axis = plt.subplots(6)
axis[0].plot(t, carrier.out, t, modulated.out)
axis[0].set_title("Carrier and modulated")

axis[1].plot(t, carrier.out, t, modulated.out, t, natural_sampled)
axis[1].set_title("Natural sampling")

axis[2].plot(t, carrier.out, t, modulated.out, t, asymmetrically_sampled, "--", t, asymmetrically_modulated)
axis[2].set_title("Uniform asymmetrical sampling")

axis[3].plot(t, carrier.out, t, modulated.out, t, symmetrically_sampled, "--", t, symmetrically_modulated)
axis[3].set_title("Uniform symmetrical sampling")

axis[4].plot(t, modulated.out, t, symmetrically_sampled, t, asymmetrically_sampled)
axis[4].set_title("Uniform sampling comparison")

axis[5].plot(t, symmetrically_modulated, t, asymmetrically_modulated)
axis[5].set_title("Uniform sampling modulation comparison")

plt.show()
