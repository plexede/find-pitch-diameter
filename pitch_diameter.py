# To calculate the size of a gear:
# The diameter of a gear from its center to its ideal meshing point can be represented as the Pitch Diameter.
# Pitch Diameter = Module * Number of Teeth
# Using this, the ideal distance between two gears can be calculated by finding the sum of both gears’ pitch diameters and dividing them by two.

# The goal is to input a ratio, and output the number of gear teeth between 3 compound gears.

MODULE = 1
CENTER_DISTANCE = 60 # mm
# centerDistance = (pitchDiameter1 + pitchDiameter2) / 2

pitchDiameter1 = MODULE * inputNumberOfTeeth

def findIdealGearSize(centerDistance, pitchDiameter1):
    idealPitchDiameter = (2 * centerDistance ) - pitchDiameter1
    idealPitchDiameter /= 2
    return idealPitchDiameter

inputNumberOfTeeth = pitchDiameter1 / MODULE
print("number of teeth on gear 1:", inputNumberOfTeeth)

# print(pitchDiameter2)

numberOfTeeth2 = idealPitchDiameter / MODULE
print("ideal number of teeth on gear 2:", numberOfTeeth2)

int(ratio) = inputNumberOfTeeth / numberOfTeeth2
print("the ratio of gear 1 to gear 2 is:", ratio, ": 1")


# find specific ratio
targetRatio = 2.5
while ratio != targetRatio
    inputNumberOfTeeth


# print(centerDistance)