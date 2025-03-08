import numpy as np

from scipy.integrate import odeint



def SIR_model(y, t, N, beta, gamma):

    S, I, R = y

    dSdt = -beta * S * I / N

    dIdt = beta * S * I / N - gamma * I

    dRdt = gamma * I

    return [dSdt, dIdt, dRdt]



# Parameters

N = 100

beta = 0.5

gamma = 0.2



# Initial conditions

y0 = [N-1, 1, 0]



# Time points

t = np.linspace(0, 75, 100)



# Solve the differential equations

ret = odeint(SIR_model, y0, t, args=(N, beta, gamma))



# Plot the results

import matplotlib.pyplot as plt

plt.plot(t, ret[:, 0], label='Susceptible')

plt.plot(t, ret[:, 1], label='Infected')

plt.plot(t, ret[:, 2], label='Recovered')

plt.xlabel('Time')

plt.ylabel('Population Size')

plt.legend()

plt.show()