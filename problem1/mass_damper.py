import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def mass_spring_damp_acc(state_of_system, time):
    """Right hand side of scipy.odeint, At each time step return
    the velocity and acceleration to evaluate the position.

    :param state_of_system: [position and velocity] as an array
    :param time: time
    :returns: [velocity and acceleration]
    :rtype: list

    """
    pos = state_of_system[0]
    vel = state_of_system[1]
    # Constants of mass damper
    spring_constant = 2.5
    damping_constant = 0.2
    mass = 1.5

    # compute the acceleration
    acc = (-spring_constant * pos - damping_constant * vel) / mass
    return [vel, acc]

    # plt.legend(loc='upper right')


INITIAL_STATE = [3.0, 0.0]
TIME = np.arange(0, 10, 0.1)
ALL_STATES = odeint(mass_spring_damp_acc, INITIAL_STATE, TIME)

fig, ax = plt.subplots()
line, = ax.plot(TIME, ALL_STATES[:, 1])
