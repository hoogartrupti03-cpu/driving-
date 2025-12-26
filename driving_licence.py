# driving_licence.py
import sys

name = sys.argv[1]
theory = float(sys.argv[2])
practical = float(sys.argv[3])
rules = float(sys.argv[4])

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
