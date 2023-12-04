# IN PROGRESS
colors = {'blue': 0, 'green': 0, 'red': 0}

def test():
    with open('Day2ScriptTest.txt', 'r', encoding="utf-8") as file:
        games = file.readlines()
        for row in games:
            game = row.split(' ')
            for x in range(len(game) - 1):
                y = game[x].strip(':,\n')
                game[x] = y
            print(game)
        file.close()


def main():
    with open('Day2Script.txt','r', encoding="utf-8") as file:
        games = file.readlines()

        file.close()


test()