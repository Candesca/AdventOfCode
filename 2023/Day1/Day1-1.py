def calibrateNumber(n):
    if len(n) == 1:
        return n + n
    if len(n) > 2:
        return n[0] + n[len(n) - 1]
    return n

def test():
    lines = [
        '1abc2',
        'pqr3stu8vwx',
        'a1b2c3d4e5f',
        'treb7uchet'
    ]
    calibrationValue = 0
    for row in lines:
        number = ''.join(x for x in row if x.isdigit())
        calibration = calibrateNumber(number)
        calibrationValue += int(calibration)
    print(calibrationValue)


def main():
    with open('Day1Script.txt', 'r', encoding="utf-8") as file:
        lines = file.readlines()
        calibrationValue = 0
        for row in lines:
            number = ''.join(x for x in row if x.isdigit())
            calibration = calibrateNumber(number)
            calibrationValue += int(calibration)
        print(calibrationValue)

    file.close()


main()
