import os
import sys
from .day17 import main
input_file = os.path.join(os.path.dirname(__file__), "input.txt")

if len(sys.argv) > 1:
    input_file = sys.argv[1]

main(input_file)
