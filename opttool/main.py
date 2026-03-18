import ast
import sys
import os
from detectors.high import HighDetectors
from detectors.medium import MediumDetectors
from ai_engine import analyse
from parser_engine import get_parser, detect_language


if len(sys.argv) < 2:
    print("Usage: python main.py <filename>")
    exit()

filename = sys.argv[1]
if not os.path.exists(filename):
    print(f"Error: file '{filename}' not found")
    exit()
code = open(filename).read()

language = detect_language(filename)
if language is None:
    print(f"Unsupported file type : {filename}")
    exit()

parser = get_parser(language)
tree = parser.parse(bytes(code, 'utf8'))

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