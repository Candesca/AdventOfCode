# Part 1
with open('Day1Script.txt', 'r', encoding="utf-8") as file:
    data = file.read()
    floor = 0
    for x in data:
        if x == '(':
            floor += 1
        else:
            floor -= 1
file.close()

print(floor)