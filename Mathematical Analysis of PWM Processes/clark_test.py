from models.signals.Signal import SineSignal
import numpy as np
import matplotlib.pyplot as plt
from transformations.Clarke import clark

t = np.linspace(0,1,100)

Vu = SineSignal(time=t)
Vv = SineSignal(phi=-120, time=t)
Vw = SineSignal(phi=+120, time=t)

fig, axs = plt.subplots(2, figsize=(10,10))
fig.suptitle("Clark transformation")
axs[0].plot(t,Vu.out,t,Vv.out,t,Vw.out)
axs[0].set_xlabel("time[s]")
axs[0].set_ylabel("V")
axs[0].legend(["Vu","Vv","Vw"])
axs[0].set_title("Time domain")

clark_transformed = clark(np.array([Vu.out, Vv.out, Vw.out]))
alpha, beta, gamma = clark(np.array([Vu.out, Vv.out, Vw.out]))

axs[1].plot(t, alpha.flat,t, beta.flat,t, gamma.flat)
axs[1].legend(["Valpha","Vbeta","Vgamma"])
axs[1].set_xlabel("time[s]")
axs[1].set_ylabel("V")
axs[1].set_title("Alpha beta gamma axis reference")

plt.show()