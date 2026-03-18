import ast
from detectors.high import HighDetectors
from detectors.medium import MediumDetectors
from ai_engine import analyse

code = open("code.py").read()
tree = ast.parse(code)

all_warnings = []

for DetectorClass in [HighDetectors, MediumDetectors]:
    detector = DetectorClass()
    detector.visit(tree)

    if hasattr(detector, 'check_attr_counts'):
        detector.check_attr_counts()

    all_warnings.extend(detector.warnings)


if all_warnings:
    for w in all_warnings:
        print(w)
else:
    print("No issues found!")

result = analyse(code, all_warnings)
print("\n--- AI Analysis ---\n")
print(result)