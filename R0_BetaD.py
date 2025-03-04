import numpy as np
import matplotlib.pyplot as plt
#from SIRP import quadratic
#from SIRP import S0


# Fixed parameters
gamma = 0.5 # Host mortality rate
alpha = 0.04   # Shedding rate of pathogen by infected hosts
mu = 0.05     # Pathogen decay rate
beta_i = 0.03  # Indirect transmission rate via environment


# Varying parameter
beta_d_range = np.linspace(0.01, 0.5, 100)  # lower bound, higher bound, and resolution

# Calculate R0 as a function of beta_d
R0_values = []
#testlist = []
#a = 1
#c = (-beta_i * S0) / mu


#b1 = S0 * beta_i
#c1 = alpha / mu
for beta_d in beta_d_range:

    R0 = (beta_d / gamma) + (beta_i / gamma) * (alpha / mu)

    #a1 = S0 * beta_d
    #d1 = (1 + (2 * (gamma ** 2)) / (mu * a1 * c1)) * b1 * c1
    #TestR0 = (1/gamma) * (2 * a1 + b1 * c1 + d1)

    #testlist.append(TestR0)
    R0_values.append(R0) # List of exact R0 values

# Plot R0 as a function of beta_d
plt.figure(figsize=(10, 6))
plt.plot(beta_d_range, R0_values, label=r'$R_0$', color='b')
# plt.plot(beta_d_range, testlist, label=r'$R_0{ Test}$', color='g')
plt.axhline(y=1, color='r', linestyle='--', label=r'$R_0 = 1$ (Threshold)')
plt.xlabel(r'$\beta_d$ (Direct Transmission Rate)', fontsize=12)
plt.ylabel(r'$R_0$ (Basic Reproduction Number)', fontsize=12)
plt.title(r'$R_0$ as a Function of $\beta_d$', fontsize=14)
plt.legend()
plt.grid()
plt.show()

# Print (parameter, R0) values
print([(round(beta_d, 3), round(R0, 3)) for beta_d, R0 in zip(beta_d_range, R0_values)])
#print([(round(beta_d, 3), round(TestR0, 3)) for beta_d, TestR0 in zip(beta_d_range, testlist)])
