# White-Nose Syndrome (WNS) Mathematical Simulation

Code for the paper *Examining the Efficacy of Mitigation Strategies Against White-Nose Syndrome (WNS) Using Mathematical Methods* (Nazriev, 2025).

## Overview

This project uses a **SIRP compartmental model** (Susceptible, Infected, Recovered, Pathogen) to simulate White-Nose Syndrome dynamics in cave-hibernating bat populations. WNS is caused by the fungus *Pseudogymnoascus destructans* and has killed over 6.7 million bats across North America since 2006.

The model captures both direct bat-to-bat transmission and indirect transmission through environmental pathogen reservoirs (soil, sediment). The basic reproduction number R_0 is derived via the Next Generation Matrix method and used to evaluate the efficacy of mitigation strategies such as vaccination, fungicide treatment, and microclimate manipulation.

### Model Parameters

| Parameter | Symbol | Description |
|-----------|--------|-------------|
| beta_d | `β_d` | Direct transmission rate (bat to bat) |
| beta_i | `β_i` | Indirect transmission rate (from pathogen) |
| gamma | `γ` | Host mortality rate |
| alpha | `α` | Host shedding rate of pathogen |
| mu | `μ` | Pathogen decay rate |

### Analyses

Three types of sensitivity analysis are performed on R_0:

1. **One-at-a-time**: Vary each parameter individually while holding the others fixed
2. **3D surface and contour plots**: Examine the joint effect of two parameters on R_0
3. **Normalized Relative Sensitivity (NRS)**: Rank parameters by their quantitative influence on R_0

## Project Structure

```
src/
├── SIR.py                              # Baseline SIR model
├── SIRP.py                             # SIRP model with pathogen compartment
├── SIRP.ipynb                          # SIRP simulation notebook
├── R0_values.py                        # R0 computation functions for each parameter
├── R0 vs Parameter/                    # One-at-a-time sensitivity analysis
│   ├── R0_Alpha.ipynb
│   ├── R0_Beta_d.ipynb
│   ├── R0_Beta_i.ipynb
│   ├── R0_Gamma.ipynb
│   └── R0_Mu.ipynb
├── Surface and Contour Plot.ipynb      # 3D surface and contour plot analysis
└── Normalized Relative Sensitivity.ipynb  # NRS sensitivity analysis
```

## Setup

1. Clone the repository:
    ```
    git clone https://github.com/nazabu/WNS-Mathematical-Simulation
    ```

2. Install dependencies:
    ```
    pip install numpy scipy matplotlib
    ```

3. Open the notebooks in `src/`:
    ```
    cd WNS-Mathematical-Simulation/src
    ```