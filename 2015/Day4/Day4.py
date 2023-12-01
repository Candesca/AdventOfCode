# Part 1 & Part 2
from hashlib import md5

init = 'yzbqklnj'
for i in range(10000000):
    h = md5((init + str(i)).encode()).hexdigest()
    if h[:6] == '000000':
        print(h)
        print(i)
        break
