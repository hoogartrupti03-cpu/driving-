name = input("Applicant name: ")
theory = float(input("Theory Test: "))
practical = float(input("Practical Test: "))
rules = float(input("Traffic Rules: "))

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

print("License Result:", result)
