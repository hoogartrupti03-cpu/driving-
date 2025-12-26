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
    rule
