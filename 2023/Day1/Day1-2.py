numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

def calibrateNumber(n):
    if len(n) == 1:
        return n + n
    if len(n) > 2:
        return n[0] + n[len(n) - 1]
    return n

def test():
    lines = [
        'two1nine',
        'eightwothree',
        'abcone2threexyz',
        'xtwone3four',
        '4nineeightseven2',
        'zoneight234',
        '7pqrstsixteen'
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


test()