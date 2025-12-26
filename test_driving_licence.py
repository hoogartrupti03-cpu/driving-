import subprocess

def run_driving(args=None):
    """Helper to run driving_licence.py and return output."""
    cmd = ["python", "driving_licence.py"]
    if args:
        cmd += [str(a) for a in args]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

def test_default_values():
    output = run_driving()
    assert "Test Applicant" in output
    assert "Qualified Driver" in output

def test_high_scores():
    output = run_driving(["Alice", 95, 90, 88])
    assert "Alice" in output
    assert "Excellent Driver" in output

def test_mid_scores():
    output = run_driving(["Bob", 70, 65, 75])
    assert "Bob" in output
    assert "Qualified Driver" in output
