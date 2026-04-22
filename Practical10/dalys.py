# Practical 10: Global Health Data Analysis
# IBI1 Practical 10
# Analyze DALYs (Disability-Adjusted Life Years) dataset using Pandas and Matplotlib

# Step 1: Import required libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Step 2: Set your working directory (CHANGE THIS PATH TO YOUR OWN FOLDER!)
# Replace the path below with the folder where your CSV file is located
os.chdir("/mnt/d/vscode_project/IBI1_2025-26/Practical10")  # Update this path!

# Step 3: Load the dataset
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# ------------------------------
# Task 1: View basic data info
# ------------------------------
print("\n=== First 5 rows of data ===")
print(dalys_data.head())

print("\n=== Data structure ===")
dalys_data.info()

print("\n=== Statistical summary ===")
print(dalys_data.describe())

# ------------------------------
# Task 2: Show first 10 rows, Year and DALYs columns (columns 3 & 4)
# Find Afghanistan's year with highest DALYs in first 10 rows
# ------------------------------
print("\n=== First 10 rows: Year and DALYs ===")
first_10 = dalys_data.iloc[0:10, [2, 3]]
print(first_10)

# Find Afghanistan's max DALYs year in first 10 entries
afghanistan_data = dalys_data.iloc[0:10]
max_idx = afghanistan_data['DALYs'].idxmax()
max_year = afghanistan_data.loc[max_idx, 'Year']
max_daly = afghanistan_data.loc[max_idx, 'DALYs']
print(f"\nAfghanistan's highest DALYs in first 10 years: {max_year}, DALYs = {max_daly}")

# ------------------------------
# Task 3: Extract Zimbabwe data using boolean indexing
# ------------------------------
zimbabwe = dalys_data.loc[dalys_data["Entity"] == "Zimbabwe"]
print("\n=== Zimbabwe data ===")
print(zimbabwe.head())

# Show Zimbabwe data year range
min_year_zim = zimbabwe['Year'].min()
max_year_zim = zimbabwe['Year'].max()
print(f"Zimbabwe data ranges from {min_year_zim} to {max_year_zim}")

# ------------------------------
# Task 4: Find countries with highest and lowest DALYs in 2019
# ------------------------------
data_2019 = dalys_data.loc[dalys_data['Year'] == 2019, ['Entity', 'DALYs']]

max_country = data_2019.loc[data_2019['DALYs'].idxmax(), 'Entity']
max_daly_2019 = data_2019['DALYs'].max()

min_country = data_2019.loc[data_2019['DALYs'].idxmin(), 'Entity']
min_daly_2019 = data_2019['DALYs'].min()

print("\n=== 2019 DALYs Extremes ===")
print(f"Highest DALYs: {max_country} ({max_daly_2019})")
print(f"Lowest DALYs: {min_country} ({min_daly_2019})")

# ------------------------------
# Task 5: Plot DALYs trend for United Kingdom
# ------------------------------
uk_data = dalys_data.loc[dalys_data['Entity'] == 'United Kingdom']

plt.figure(figsize=(10, 5))
plt.plot(uk_data['Year'], uk_data['DALYs'], 'b-o', label='United Kingdom')
plt.title('DALYs Rate Over Time (United Kingdom)')
plt.xlabel('Year')
plt.ylabel('DALYs Rate')
plt.xticks(uk_data['Year'], rotation=-90)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("uk_dalys_trend.png",dpi=300)
plt.close()

# ------------------------------
# Task 6: Optional - Plot China vs UK trend
# ------------------------------
china_data = dalys_data.loc[dalys_data['Entity'] == 'China']

plt.figure(figsize=(10, 5))
plt.plot(uk_data['Year'], uk_data['DALYs'], 'b-o', label='UK')
plt.plot(china_data['Year'], china_data['DALYs'], 'r-s', label='China')
plt.title('DALYs Rate: China vs United Kingdom')
plt.xlabel('Year')
plt.ylabel('DALYs Rate')
plt.xticks(rotation=-90)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("china_uk_comparison.png", dpi=300)
plt.close()
