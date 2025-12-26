import sys

# Check if arguments are provided
if len(sys.argv) == 5:
    name = sys.argv[1]
    theory = float(sys.argv[2])
    practical = float(sys.argv[3])
    rules = float(sys.argv[4])
else:
    print("No command-line arguments provided, using default test data.")
    name = "Test Applicant"
    theory = 90
    practical = 85
    rules = 80

avg = (theory + practical + rules) / 3

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

print(f"Applicant: {name}")
print(f"Average Score: {avg}")
print(f"Evaluation: {result}")
