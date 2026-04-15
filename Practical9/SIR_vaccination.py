import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Model parameters
N = 10000
beta = 0.3
gamma = 0.05
time_steps = 1000
# 0% to 100% vaccination rates (11 points)
vaccination_rates = [round(i/10, 1) for i in range(11)]

plt.figure(figsize=(6, 4), dpi=150)
colors = cm.viridis(np.linspace(0, 1, len(vaccination_rates)))

# Simulate for each vaccination rate
for idx, v in enumerate(vaccination_rates):
    n_vaccinated = int(N * v)
    # Ensure initial susceptible is non-negative (critical fix)
    S = max(N - 1 - n_vaccinated, 0)
    I = 1
    R = 0
    
    I_list = [I]
    
    for t in range(time_steps):
        # Only run infection if there are susceptible people
        if S > 0:
            infection_prob = beta * (I / N)
            new_infected = np.random.binomial(S, infection_prob)
        else:
            new_infected = 0
        
        # Only run recovery if there are infected people
        if I > 0:
            new_recovered = np.random.binomial(I, gamma)
        else:
            new_recovered = 0
        
        # Update states
        S -= new_infected
        I += new_infected - new_recovered
        R += new_recovered
        
        # Enforce non-negative values for all compartments
        S = max(S, 0)
        I = max(I, 0)
        R = max(R, 0)
        
        I_list.append(I)
    
    plt.plot(I_list, label=f'Vaccination {int(v*100)}%', color=colors[idx])

plt.xlabel('Time steps')
plt.ylabel('Number of infected individuals')
plt.title('SIR Model with Vaccination')
plt.legend(loc='upper right', fontsize=6)
plt.tight_layout()
plt.savefig('SIR_vaccination_plot.png', bbox_inches='tight')

