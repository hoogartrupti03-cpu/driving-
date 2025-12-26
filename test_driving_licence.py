# test_driving_licence.py
from driving_licence_app import driving_report

def test_driving_report():
    expected_output = (
        "Applicant: Test Applicant\n"
        "Average Score: 75.00\n"
        "Evaluation: Qualified Driver"
    )
    assert driving_report("Test Applicant", 80, 75, 70) == expected_output

    expected_output2 = (
        "Applicant: Alice\n"
        "Average Score: 90.00\n"
        "Evaluation: Excellent Driver"
    )
    assert driving_report("Alice", 95, 90, 85) == expected_output2
