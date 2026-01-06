import sys
# Default values
default_name = "Test Applicant"
default_theory = 80
default_practical = 75
default_rules = 70

# --- Step 1: Use command-line arguments if provided ---
if len(sys.argv) == 5:
    name = sys.argv[1]
    try:
        theory = float(sys.argv[2])
        practical = float(sys.argv[3])
        rules = float(sys.argv[4])
    except ValueError:
        print("Invalid command-line arguments. Using default values.")
        name = default_name
        theory = default_theory
        practical = default_practical
        rules = default_rules
else:
    # --- Step 2: No arguments, use default values ---
    name = default_name
    theory = default_theory
    practical = default_practical
    rules = default_rules

# --- Step 3: Calculate average ---
avg = (theory + practical + rules) / 3

# --- Step 4: Determine evaluation ---
if avg >= 90:
    result = "Excellent Driver"
elif avg >= 80:
    result = "Safe Driver"
elif avg >= 65:
    result = "Qualified Driver"
elif avg >= 50:
    result = "Conditional Pass"
elif avg >= 40:
    result = "Re-Test Required"
else:
    result = "Fail"

# --- Step 5: Print results ---
print("--- Driving License Evaluation ---")
print(f"Applicant: {name}")
print(f"Average Score: {avg:.2f}")
print(f"Evaluation: {result}")
