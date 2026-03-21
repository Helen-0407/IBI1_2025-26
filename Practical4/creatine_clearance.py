# Pseudocode plan
# 1. Define input variables: age (years), weight (kg), gender, creatine concentration Cr (μmol/l)
# 2. Check if input values are within the valid ranges
# 3. If inputs are valid, calculate CrCl using the Cockcroft-Gault Equation
# 4. If inputs are invalid, prompt the variables that need correction
# 5. Print the calculated CrCl result or error prompt

# Actual code
# Define input variables (can be modified for testing)
age = 20               # Age (years)
weight = 65            # Weight (kg)
gender = "male"      # Gender: male/female
cr = 80                # Creatine concentration (μmol/l)

# Initialize validity flag
is_valid = True
error_msg = "Variables to correct: "

# Check input ranges
if age >= 100 or age < 0:
    is_valid = False
    error_msg += "age "
if weight <= 20 or weight >= 80:
    is_valid = False
    error_msg += "weight "
if cr <= 0 or cr >= 100:
    is_valid = False
    error_msg += "creatine concentration "
if gender not in ["male", "female"]:
    is_valid = False
    error_msg += "gender "

# Calculate Creatine Clearance (CrCl)
if is_valid:
    # Basic formula
    crcl_base = (140 - age) * weight / (72 * cr)
    # Multiply by 0.85 for female
    if gender == "female":
        crcl = crcl_base * 0.85
    else:
        crcl = crcl_base
    # Print result (2 decimal places)
    print(f"Creatine Clearance (CrCl): {crcl:.2f} ml/min")
else:
    # Print error prompt
    print(error_msg)