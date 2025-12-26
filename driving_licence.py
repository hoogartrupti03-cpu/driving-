import sys

# Ensure exactly 4 arguments are provided
if len(sys.argv) != 5:
    print("Usage: python driving_licence.py <Name> <Theory> <Practical> <Rules>")
    print("Example: python driving_licence.py John 95 92 93")
    sys.exit(1)  # Exit with error code

# Get command-line arguments
name = sys.argv[1]
theory = float(sys.argv[2])
practical = float(sys.argv[3])
rules = float(sys.argv[4])

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
print(f"Average Score: {avg}")
print(f"Evaluation: {result}")
