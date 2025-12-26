# test_driving_licence.py
from driving_licence import driving_report

def test_default_report():
    expected_output = (
        "Applicant: Test Applicant\n"
        "Average Score: 75.00\n"
        "Evaluation: Qualified Driver"
    )
    assert driving_report() == expected_output

def test_custom_report():
    expected_output = (
        "Applicant: Alice\n"
        "Average Score: 90.00\n"
        "Evaluation: Excellent Driver"
    )
    assert driving_report("Alice", 95, 90, 85) == expected_output
