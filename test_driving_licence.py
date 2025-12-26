# test_driving_licence.py
from driving_licence import driving_report

def test_default_report():
    expected_output = (
        "Applicant: Test Applicant\n"
        "Average Score: 75.00\n"
        "Evaluation: Qualified Driver"
    )
    assert driving_report() == expected_output

def test_safe_driver():
    expected_output = (
        "Applicant: Alice\n"
        "Average Score: 85.00\n"
        "Evaluation: Safe Driver"
    )
    assert driving_report("Alice", 90, 80, 85) == expected_output

def test_excellent_driver():
    expected_output = (
        "Applicant: Bob\n"
        "Average Score: 95.00\n"
        "Evaluation: Excellent Driver"
    )
    assert driving_report("Bob", 95, 97, 93) == expected_output
