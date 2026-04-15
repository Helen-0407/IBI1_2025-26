import numpy as np
import matplotlib.pyplot as plt

# Model parameters
N = 10000
beta = 0.3
gamma = 0.05
time_steps = 1000

# Initial state
S = N - 1
I = 1
R = 0

# Lists to store time series
S_list = [S]
I_list = [I]
R_list = [R]

# Simulation loop
for t in range(time_steps):
    # Stochastic infection
    infection_prob = beta * (I / N)
    new_infected = np.random.binomial(S, infection_prob)
    
    # Stochastic recovery
    new_recovered = np.random.binomial(I, gamma)
    
    # Update states
    S -= new_infected
    I += new_infected - new_recovered
    R += new_recovered
    
    # Ensure non-negative
    S = max(S, 0)
    I = max(I, 0)
    R = max(R, 0)
    
    # Append data
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

# Plot results
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(S_list, label='Susceptible')
plt.plot(I_list, label='Infected')
plt.plot(R_list, label='Recovered')
plt.xlabel('Time steps')
plt.ylabel('Number of individuals')
plt.title('Stochastic SIR Model')
plt.legend()
plt.savefig('SIR_plot.png', bbox_inches='tight')
