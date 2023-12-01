def test():
    test1 = 'qjhvhtzxzqqjkmpb'
    test2 = 'xxyxx'
    test3 = 'uurcxstgmygtbstg'
    test4 = 'ieodomkazucvgmuy'

    print(str(naughtyOrNice(test1)))
    print(str(naughtyOrNice(test2)))
    print(str(naughtyOrNice(test3)))
    print(str(naughtyOrNice(test4)))


def main():
    with open('Day5Script.txt', 'r', encoding="utf-8") as file:
        names = file.readlines()
        niceNames = 0
        for name in names:
            if str(naughtyOrNice(name)) == 'nice':
                niceNames += 1

        print(niceNames)
    file.close()


def checkSeparatedRepeatLetters(name):
    count = 0
    combo = []
    for l in name:
        if name[count] + name[count + 1] in combo:
            return True
        combo.append(name[count] + name[count + 1])
        count += 1
        if count + 1 >= len(name):
            break
    return False


def checkDoubleCombos(name):
    count = 0
    for l in name:
        if name[count] == name[count + 2]:
            return True
        count += 1
        if count + 2 >= len(name):
            break
    return False


def naughtyOrNice(name):
    if checkSeparatedRepeatLetters(name) and checkDoubleCombos(name):
        return 'nice'
    return 'naughty'

# test()

main()