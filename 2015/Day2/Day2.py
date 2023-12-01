# Part 1
def calculateSqFeet(a, b, c):
    aS, bS, cS = (a * b), (b * c), (c * a)
    return (aS * 2) + (bS * 2) + (cS * 2) + min(aS, bS, cS)


with open('Day2Script.txt', 'r', encoding="utf-8") as file:
    totalSqFeet = 0
    for x in file.readlines():
        a, b, c = x.split('x')
        totalSqFeet += calculateSqFeet(int(a), int(b), int(c))
file.close()

print(totalSqFeet)