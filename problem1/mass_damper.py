import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def mass_spring_damp_acc(state, t):
    pos = state[0]
    vel = state[1]
    # Constants of mass damper
    k = 2.5
    c = 0.2
    m = 1.5

    # compute the acceleration
    acc = (-k * pos / m - c * vel)
    return [vel, acc]


state0 = [3.0, 0.0]
t = np.arange(0, 10, 0.1)
state = odeint(mass_spring_damp_acc, state0, t)
plt.figure(1)
plt.subplot(211)
plt.plot(t, state[:, 0], label='Position')
plt.legend(loc='upper right')
plt.subplot(212)
plt.plot(t, state[:, 1], label='Velocity')
plt.legend(loc='upper right')
# plt.show()
