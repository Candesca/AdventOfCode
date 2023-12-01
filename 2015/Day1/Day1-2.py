# Part 2
with open('Day1Script.txt', 'r', encoding="utf-8") as file:
    data = file.read()
    position = 0
    floor = 0
    for x in data:
        position += 1
        if x == '(':
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            print(position)
file.close()