# Pseudocode plan
# 1. Define initial variables: initial infected number, growth rate, total number of students in the class
# 2. Initialize days and the number of infected people on the current day
# 3. Loop to calculate the daily number of infected people until the infected number ≥ total students
# 4. Print the daily infected number and total days taken

# Actual code
# Initial parameters
initial_infected = 5  # Initial number of infected students
growth_rate = 0.4     # 24-hour growth rate (40%)
total_students = 91   # Total number of students in the class

# Initialize variables
current_infected = initial_infected
days = 0

# Print initial state
print(f"Day {days}, Infected number: {current_infected}")

# Loop to calculate infected number
while current_infected < total_students:
    # Calculate newly infected number on the current day
    new_infected = current_infected * growth_rate
    current_infected += new_infected
    days += 1
    # Print daily infected number (1 decimal place for simplified display)
    print(f"Day {days}, Infected number: {current_infected:.1f}")

# Print total days
print(f"\nTotal days to infect all 91 students: {days} days")