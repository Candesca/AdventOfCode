# Part 1 >> Part 2
def test():
    # directions = '^v'
    # directions = '^>v<'
    directions = '^v^v^v^v^v'
    santaRoute = directions[::2]
    roboSantaRoute = directions[1::2]

    santaMap = visitHouses(santaRoute)
    roboSantaMap = visitHouses(roboSantaRoute)

    newHouse = checkHouseOverlap(santaMap, roboSantaMap)

    print(newHouse)


def traverse(x, y, direction):
    newX = x
    newY = y
    if direction == '^':
        newY += 1
    elif direction == 'v':
        newY -= 1
    elif direction == '>':
        newX += 1
    elif direction == '<':
        newX -= 1

    return newX, newY


def visitHouses(directions):
    x = 0
    y = 0
    neighborhood = {'0x0': 0}
    for item in directions:
        newX, newY = traverse(x, y, item)
        x = newX
        y = newY
        if (str(newX) + 'x' + str(newY)) not in neighborhood:
            neighborhood[str(newX) + 'x' + str(newY)] = 1
        else:
            neighborhood[str(newX) + 'x' + str(newY)] += 1
    return neighborhood


def checkHouseOverlap(map1, map2):
    for house in map2:
        if house not in map1:
            map1[house] = 1

    return len(map1)


def smushMaps(map1, map2):
    newDict = {}
    newDict.update(map1)
    newDict.update(map2)
    return newDict

def main():
    with open('Day3Script.txt', 'r', encoding="utf-8") as file:
        directions = file.read()

        santaRoute = directions[::2]
        roboSantaRoute = directions[1::2]

        santaMap = visitHouses(santaRoute)
        roboSantaMap = visitHouses(roboSantaRoute)

        # print(smushMaps(santaMap, roboSantaMap))
        # mapLength = len(smushMaps(santaMap, roboSantaMap))
        # print(mapLength)

        newHouse = checkHouseOverlap(santaMap, roboSantaMap)
    file.close()

    print(newHouse)

main()
# test()
