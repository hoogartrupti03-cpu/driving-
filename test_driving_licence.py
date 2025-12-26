# test_driving_licence_app.py
import sys
from driving_licence_app import main, evaluate

def test_evaluate():
    assert evaluate(95) == "Excellent Driver"
    assert evaluate(85) == "Safe Driver"
    assert evaluate(70) == "Qualified Driver"
    assert evaluate(55) == "Conditional Pass"
    assert evaluate(45) == "Re-Test Required"
    assert evaluate(30) == "Fail"

def test_default_values(monkeypatch, capsys):
    # Simulate no command-line arguments
    monkeypatch.setattr(sys, "argv", ["driving_licence_app.py"])
    main()
    captured = capsys.readouterr()
    assert "Applicant: Test Applicant" in captured.out
    assert "Average Score: 75.00" in captured.out
    assert "Evaluation: Qualified Driver" in captured.out

def test_given_values(monkeypatch, capsys):
    # Simulate passing command-line arguments
    monkeypatch.setattr(sys, "argv", ["driving_licence_app.py", "Alice", "95", "90", "85"])
    main()
    captured = capsys.readouterr()
    assert "Applicant: Alice" in captured.out
    assert "Average Score: 90.00" in captured.out
    assert "Evaluation: Excellent Driver" in captured.out
