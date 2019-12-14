import math

input_file = open('input-day1.txt', 'r')
input = []
fuel = []
accumulated_fuel = 0

for line in input_file:
    input.append(int(line.strip('\n')))

for mass in input:
    fuel.append((math.floor(mass / 3)) - 2)

for fuel_element in fuel:
    accumulated_fuel += fuel_element

print(accumulated_fuel)
