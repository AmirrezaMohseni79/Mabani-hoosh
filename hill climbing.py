import random
import math


pi=3.14
# Ackley function
def ackley(x, y):
    return -20.0 * math.exp(-0.2 * math.sqrt(0.5 * (x**2 + y**2))) - math.exp(0.5 * (math.cos(2 * pi * x) + math.cos(2 * pi * y))) + math.e + 20

# Initial position
x = (random.uniform(-1, 1), random.uniform(-1, 1))

# Step size
step = 0.1

# Minimum value found
min_value = ackley(x[0], x[1])

while True:
    x_new = (x[0] + step * (random.uniform(-1, 1)), x[1] + step * (random.uniform(-1, 1)))
    value_new = ackley(x_new[0], x_new[1])
    if value_new <= min_value:  
        x = x_new
        min_value = value_new
    else:
        step *= 0.9
    if min_value < 0.1 and step < 0.1:
        break

print(f"Minimum value: {min_value}")
print(f"Coordinates: {x}")