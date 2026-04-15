# PSEUDOCODE & LOGIC FOR 2D SPATIAL SIR MODEL
# 1. Create a 100x100 grid (all susceptible: 0)
# 2. Randomly infect one cell (set to 1)
# 3. For each time step:
#    a. Find all currently infected cells
#    b. For each infected cell, try to infect 8 neighboring cells
#    c. Infected cells recover with probability gamma
#    d. Apply new infections to the grid
# 4. Save heatmaps at key time steps

import numpy as np
import matplotlib.pyplot as plt

# Grid and epidemic parameters
size = 100
beta = 0.3
gamma = 0.05
time_steps = 100

# 0 = Susceptible, 1 = Infected, 2 = Recovered
population = np.zeros((size, size), dtype=int)

# Random initial infection
outbreak = np.random.choice(size, 2)
population[outbreak[0], outbreak[1]] = 1

# Plot initial state
plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.title('Time 0 (Initial Infection)')
plt.colorbar(label='0=Susceptible, 1=Infected, 2=Recovered')
plt.tight_layout()
plt.savefig('spatial_SIR_time0.png', bbox_inches='tight')
plt.close()

# 8 surrounding neighbors
directions = [(-1,-1), (-1,0), (-1,1),
              (0,-1),          (0,1),
              (1,-1),  (1,0), (1,1)]

# Main simulation loop
for step in range(time_steps):
    new_infections = np.zeros_like(population)
    infected_positions = np.argwhere(population == 1)
    
    # Spread infection to neighbors
    for (i, j) in infected_positions:
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < size and 0 <= nj < size:
                if population[ni, nj] == 0 and np.random.rand() < beta:
                    new_infections[ni, nj] = 1
    
    # Recover infected individuals
    for (i, j) in infected_positions:
        if np.random.rand() < gamma:
            population[i, j] = 2
    
    # Apply new infections to grid
    population[new_infections == 1] = 1
    
    # Save plots at important time steps
    if step in [9, 49, 99]:
        plt.figure(figsize=(6,4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f'Time {step+1}')
        plt.colorbar(label='0=Susceptible, 1=Infected, 2=Recovered')
        plt.tight_layout()
        plt.savefig(f'spatial_SIR_time{step+1}.png', bbox_inches='tight')
        plt.close()