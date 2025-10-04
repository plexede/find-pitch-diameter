# To calculate the size of a gear:
# The diameter of a gear from its center to its ideal meshing point can be represented as the Pitch Diameter.
# Pitch Diameter = Module * Number of Teeth
# Using this, the ideal distance between two gears can be calculated by finding the sum of both gears’ pitch diameters and dividing them by two.
module = 1
# var centerDistance # mm distance between two axles

numberOfTeeth1 = 80
numberOfTeeth2 = 40
pitchDiameter1 = module * numberOfTeeth1
pitchDiameter2 = module * numberOfTeeth2

# centerDistance = (pitchDiameter1 + pitchDiameter2) / 2

centerDistance = 60 # mm
idealPitchDiameter = (2 * centerDistance ) - pitchDiameter1
idealPitchDiameter /= 2

numberOfTeeth1 = pitchDiameter1 / module
print("number of teeth on gear 1:", numberOfTeeth1)

# print(pitchDiameter2)

numberOfTeeth2 = idealPitchDiameter / module
print("ideal number of teeth on gear 2:", numberOfTeeth2)

print("the ratio of gear 1 to gear 2 is:", int(numberOfTeeth1 / numberOfTeeth2), ": 1")


# print(centerDistance)