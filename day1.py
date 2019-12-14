import math

# Part 1

input_file = open('input-day1-part1.txt', 'r')
input = []
fuels = []
accumulated_fuel = 0

for line in input_file:
    input.append(int(line.strip('\n')))

for mass in input:
    fuels.append((math.floor(mass / 3)) - 2)

for fuel in fuels:
    accumulated_fuel += fuel

print(accumulated_fuel)

# Part 2

fuels_part2 = []
acc_fuels = 0

for fuel in fuels:
    acc = fuel
    while fuel > 0:
        fuel = (math.floor(fuel / 3)) - 2
        if (fuel > 0):
            acc += fuel
    fuels_part2.append(acc)

for fuel in fuels_part2:
    acc_fuels += fuel
print(acc_fuels)
