# TASK 3: Population Growth Rate Analysis
# ==============================================
# PSEUDOCODE:
# 1. Create a dictionary to store 2020 and 2024 population data for each country
# 2. Define a function to calculate percentage population change (per the given formula)
# 3. Loop through the dictionary: calculate % change for each country and store in a new dict
# 4. Print the percentage change for each country (2 decimal places)
# 5. Sort the % change dict in DESCENDING order (largest increase to largest decrease)
# 6. Print the sorted population changes
# 7. Identify the country with the largest increase and largest decrease
# 8. Print these two countries with clear statements
# 9. Create a well-labelled bar chart for population % change (add grid for readability)
import matplotlib.pyplot as plt
# 1. Define population data (2020, 2024) in millions

population_data = {
    'UK': (66.7, 69.2),
    'China': (1426, 1410),
    'Italy': (59.4, 58.9),
    'Brazil': (208.6, 212.0),
    'USA': (331.6, 340.1)
}

# 2. Calculate percentage population change for each country
pop_percent_change = {}
for country, (pop2020, pop2024) in population_data.items():
    percent_change = ((pop2024 - pop2020) / pop2020) * 100
    pop_percent_change[country] = percent_change

# 3. Print percentage change for each country
print("=== TASK 3: Population Growth Rate Analysis ===")
print("Population percentage change (2020-2024) for each country:")
for country, pct in pop_percent_change.items():
    print(f"{country}: {pct:.2f}%")

# 4. Sort percentage change in DESCENDING order
sorted_pop = sorted(pop_percent_change.items(), key=lambda x: x[1], reverse=True)
print("\nPopulation change sorted from largest increase to largest decrease:")
for country, pct in sorted_pop:
    print(f"{country}: {pct:.2f}%")

# 5. Identify largest increase and largest decrease
largest_increase = sorted_pop[0]
largest_decrease = sorted_pop[-1]
print(f"\nCountry with the largest population increase: {largest_increase[0]} ({largest_increase[1]:.2f}%)")
print(f"Country with the largest population decrease: {largest_decrease[0]} ({largest_decrease[1]:.2f}%)")

# 6. Plot well-labelled bar chart for population percentage change
plt.figure(figsize=(9, 6))
countries = list(pop_percent_change.keys())
pct_changes = list(pop_percent_change.values())
# Plot bars: color red for decrease, green for increase
colors = ['red' if p < 0 else 'green' for p in pct_changes]
plt.bar(countries, pct_changes, color=colors)
# Add labels, title and horizontal grid
plt.xlabel('Country', fontsize=12)
plt.ylabel('Population Percentage Change (%)', fontsize=12)
plt.title('Population Percentage Change (2020-2024) for 5 Countries', fontsize=14, pad=20)
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)  # Add zero line for reference
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()