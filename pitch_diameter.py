# To calculate the size of a gear:
# The diameter of a gear from its center to its ideal meshing point can be represented as the Pitch Diameter.
# Pitch Diameter = Module * Number of Teeth
# Using this, the ideal distance between two gears can be calculated by finding the sum of both gears’ pitch diameters and dividing them by two.

# The goal is to input a ratio, and output the number of gear teeth between 3 compound gears.

import random

MODULE = 1
CENTER_DISTANCE = 60 # mm
TARGET_RATIO = 1.5 # ratio to be solved for
# centerDistance = (pitchDiameter1 + pitchDiameter2) / 2
ratioFound = False
inputNumberOfTeeth = 1
while not ratioFound:
    pitchDiameter1 = MODULE * inputNumberOfTeeth

    def findIdealGearSize(centerDistance, pitchDiameter1):
        idealPitchDiameter = (2 * centerDistance ) - pitchDiameter1
        idealPitchDiameter /= 2
        return idealPitchDiameter

    # if not a whole number, discard
    numberOfTeeth2 = findIdealGearSize(CENTER_DISTANCE, pitchDiameter1) / MODULE
    ratio = inputNumberOfTeeth / numberOfTeeth2
    if (numberOfTeeth2 % 1) == 0: # if it is a whole number
        if ratio >= TARGET_RATIO:
            ratioFound = True
        else:
            print(f"Tried {inputNumberOfTeeth} teeth on gear 1, gives {int(numberOfTeeth2)} teeth on gear 2 with a ratio of {ratio}:1")
    inputNumberOfTeeth += 1 # increment and try again
pitchDiameter2 = MODULE * numberOfTeeth2
print(f"Gear 1: {inputNumberOfTeeth} teeth, Pitch Diameter: {pitchDiameter1} mm")
print(f"Gear 2: {int(numberOfTeeth2)} teeth, Pitch Diameter: {pitchDiameter2} mm")
print(f"Ratio: {ratio}:1")