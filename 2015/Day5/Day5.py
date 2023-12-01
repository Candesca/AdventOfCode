def test():
    test1 = 'ugknbfddgicrmopn'
    test2 = 'aaa'
    test3 = 'jchzalrnumimnmhp'
    test4 = 'haegwjzuvuyypxyu'
    test5 = 'dvszwmarrgswjxmb'

    print(str(naughtyOrNice(test1)))
    print(str(naughtyOrNice(test2)))
    print(str(naughtyOrNice(test3)))
    print(str(naughtyOrNice(test4)))
    print(str(naughtyOrNice(test5)))


def main():
    with open('Day5Script.txt', 'r', encoding="utf-8") as file:
        names = file.readlines()
        niceNames = 0
        for name in names:
            if str(naughtyOrNice(name)) == 'nice':
                niceNames += 1

        print(niceNames)
    file.close()


def checkVowels(name):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowelCount = 0
    for l in name:
        if l in vowels:
            vowelCount += 1
        if vowelCount >= 3:
            return True
    return False


def checkConsecutiveLetters(name):
    count = 0
    for l in name:
        if name[count] == name[count + 1]:
            return True
        count += 1
        if count + 1 >= len(name):
            break
    return False


def checkBadCombos(name):
    count = 0
    badCombos = ['ab', 'cd', 'pq', 'xy']
    for combo in name:
        if name[count] + name[count + 1] in badCombos:
            return True
        count += 1
        if count + 1 >= len(name):
            break
    return False


def naughtyOrNice(name):
    if not checkBadCombos(name):
        if checkVowels(name) and checkConsecutiveLetters(name):
            return 'nice'
    return 'naughty'

# test()

main()