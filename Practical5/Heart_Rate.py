
# TASK 2: Heart Rate Analysis
# ==============================================
# PSEUDOCODE:
# 1. Define the list of resting heart rates from the dataset
# 2. Calculate the number of patients (length of the list) and mean heart rate
# 3. Print a sentence with patient count and mean heart rate (2 decimal places)
# 4. Initialize counters for Low/Normal/High heart rate categories
# 5. Loop through each heart rate: increment counter based on category rules
# 6. Print the count for each category
# 7. Identify the category with the largest number of patients
# 8. Print the largest category with a clear statement
# 9. Create a well-labelled pie chart for category distribution (add labels/percentages)
import matplotlib.pyplot as plt
# 1. Define heart rate dataset
heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]

# 2. Calculate patient count and mean heart rate
patient_count = len(heart_rates)
mean_hr = sum(heart_rates) / patient_count

# Print patient count and mean heart rate
print("=== TASK 2: Heart Rate Analysis ===")
print(f"There are {patient_count} patients in the dataset, and the mean resting heart rate is {mean_hr:.2f} bpm.")

# 3. Initialize category counters
low_hr = 0
normal_hr = 0
high_hr = 0

# 4. Categorize each heart rate
for hr in heart_rates:
    if hr < 60:
        low_hr += 1
    elif 60 <= hr <= 120:
        normal_hr += 1
    else:
        high_hr += 1

# Print category counts
print(f"Heart rate category counts - Low: {low_hr}, Normal: {normal_hr}, High: {high_hr}")

# 5. Identify the largest category
hr_categories = {
    'Low': low_hr,
    'Normal': normal_hr,
    'High': high_hr
}
largest_category = max(hr_categories, key=hr_categories.get)
print(f"The category with the largest number of patients is: {largest_category}\n")

# 6. Plot well-labelled pie chart for heart rate categories
plt.figure(figsize=(7, 7))
sizes = [low_hr, normal_hr, high_hr]
labels = ['Low (<60 bpm)', 'Normal (60-120 bpm)', 'High (>120 bpm)']
colors = ['lightcoral', 'lightgreen', 'lightskyblue']
# Plot pie chart with percentages and no shadow
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, shadow=False)
plt.title('Distribution of Resting Heart Rate Categories', fontsize=14, pad=20)
plt.axis('equal')  # Ensure pie chart is a perfect circle
plt.tight_layout()
plt.show()