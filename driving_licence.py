import sys

# Check for exactly 4 arguments
if len(sys.argv) != 5:
    print("Usage: python driving_licence.py <Name> <Theory> <Practical> <Rules>")
    print("Example: python driving_licence.py John 95 92 93")
    sys.exit(1)  # Exit with error code

# Get command-line arguments
name = sys.argv[1]
try:
    theory = float(sys.argv[2])
    practical = float(sys.argv[3])
    rules = float(sys.argv[4])
except ValueError:
    print("Error: Theory, Practical, and Rules scores must be numbers.")
    sys.exit(1)

# Calculate average
avg = (theory + practical + rules) / 3

# Determine evaluation
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

# Print result
print(f"Applicant: {name}")
print(f"Average Score: {avg:.2f}")
print(f"Evaluation: {result}")
