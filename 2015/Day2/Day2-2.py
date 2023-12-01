# Part 2
import numpy

def calculateRibbon(dimensions):
    volume = numpy.prod(dimensions)
    sides = removeMax(dimensions)
    return (sides[0] * 2) + (sides[1] * 2) + volume

def removeMax(dimensions):
    dimensions.remove(max(dimensions))
    return dimensions


with open('Day2Script.txt', 'r', encoding="utf-8") as file:
    totalRibbon = 0
    for x in file.readlines():
        lst = [int(i) for i in x.split('x')]
        totalRibbon += calculateRibbon(lst)
file.close()

print(totalRibbon)