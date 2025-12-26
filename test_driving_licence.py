# test_driving_licence_app.py
from driving_licence_app import main, evaluate

def test_evaluate():
    # Test all evaluation categories
    assert evaluate(95) == "Excellent Driver"
    assert evaluate(85) == "Safe Driver"
    assert evaluate(70) == "Qualified Driver"
    assert evaluate(55) == "Conditional Pass"
    assert evaluate(45) == "Re-Test Required"
    assert evaluate(30) == "Fail"

def test_default_values(monkeypatch, capsys):
    # Simulate no command-line arguments, so defaults are used
    import sys
    monkeypatch.setattr(sys, "argv", ["driving_licence_app.py"])
    
    # Run main function
    main()
    
    # Capture printed output
    captured = capsys.readouterr()
    
    # Check default values appear in output
    assert "Applicant: Test Applicant" in captured.out
    assert "Average Score: 75.00" in captured.out
    assert "Evaluation: Qualified Driver" in captured.out
