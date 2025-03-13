import numpy as np

'''Alpha R0 Values'''
def alpha_R0_values():
    # Fixed parameters
    gamma = 0.5 # Host mortality rate
    mu = 0.05     # Pathogen decay rate
    beta_d = 0.05  # Direct transmission rate
    beta_i = 0.03  # Indirect transmission rate via environment

    # Varying parameter (lower bound, higher bound, and resolution)
    alpha_range = np.linspace(0.01, 0.5, 100)

    R0_values = []
    for alpha in alpha_range:
        R0 = (beta_d / gamma) + (beta_i / gamma) * (alpha / mu)
        R0_values.append(R0) # List of exact R0 values for alpha

    return R0_values





'''Beta_D R0 Values'''
def beta_d_R0_values():
    # Fixed parameters
    gamma = 0.5  # Host mortality rate
    alpha = 0.04  # Shedding rate of pathogen by infected hosts
    mu = 0.05  # Pathogen decay rate
    beta_i = 0.03  # Direct transmission rate via environment

    # Varying parameter
    beta_d_range = np.linspace(0.01, 0.5, 100)  # lower bound, higher bound, and resolution

    R0_values = []

    for beta_d in beta_d_range:
        R0 = (beta_d / gamma) + (beta_i / gamma) * (alpha / mu)
        R0_values.append(R0)  # List of exact R0 values

    return R0_values




'''Beta_I R0 Values'''
def beta_i_R0_values():
    # Fixed parameters
    gamma = 0.5 # Host mortality rate
    alpha = 0.04   # Shedding rate of pathogen by infected hosts
    mu = 0.05     # Pathogen decay rate
    beta_d = 0.03  # Indirect transmission rate via environment


    # Varying parameter (lower bound, higher bound, and resolution)
    beta_i_range = np.linspace(0.01, 0.5, 100)

    R0_values = []

    for beta_i in beta_i_range:
        R0 = (beta_d / gamma) + (beta_i / gamma) * (alpha / mu)
        R0_values.append(R0) # List of exact R0 values

    return R0_values



'''Gamma R0 Values'''
def gamma_R0_values():
    # Fixed parameters
    alpha = 0.04   # Shedding rate of pathogen by infected hosts
    mu = 0.05     # Pathogen decay rate
    beta_d = 0.05  # Direct transmission rate
    beta_i = 0.03  # Indirect transmission rate via environment

    # Varying parameter (lower bound, higher bound, and resolution)
    gamma_range = np.linspace(0.01, 0.5, 100)

    R0_values = []

    for gamma in gamma_range:
        R0 = (beta_d / gamma) + (beta_i / gamma) * (alpha / mu)
        R0_values.append(R0) # List of exact R0 values

    return R0_values




'''Mu R0 Values'''
def mu_R0_values():
    # Fixed parameters
    gamma = 0.5 # Host mortality rate
    alpha = 0.04   # Shedding rate of pathogen by infected hosts
    beta_d = 0.05  # Direct transmission rate
    beta_i = 0.03  # Indirect transmission rate via environment

    # Varying parameter (lower bound, higher bound, and resolution)
    mu_range = np.linspace(0.01, 0.5, 100)

    R0_values = []

    for mu in mu_range:
        R0 = (beta_d / gamma) + (beta_i / gamma) * (alpha / mu)
        R0_values.append(float(R0)) # List of exact R0 values

    return R0_values

