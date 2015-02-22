# Shipping calculator
import math
v = int(raw_input("> "))

cube = v ** (1.0/3)
sphere = ((3 * v) / (4 * math.pi)) ** (1.0/3)
print cube
print sphere