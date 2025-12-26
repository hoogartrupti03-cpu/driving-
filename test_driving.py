import subprocess

# Test cases: [name, theory, practical, rules]
# Use None for any value to test default behavior
test_cases = [
    ["Alice", 95, 90, 88],      # Normal input
    ["Bob", 70, 65, 75],        # Another normal input
    ["Carol", 85, 80, 82],      # Another normal input
    [None, None, None, None],   # Test default values
]

print("--- Running Driving License Tests ---")

for i, case in enumerate(test_cases, start=1):
    print(f"\n--- Test Case {i} ---")
    
    # Prepare command arguments
    if all(v is not None for v in case):
        cmd = ["python", "driving_licence.py"] + [str(v) for v in case]
    else:
        cmd = ["python", "driving_licence.py"]  # No arguments → defaults
    
    # Run the driving_licence.py program
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error running driving_licence.py:")
        print(e.stderr)
