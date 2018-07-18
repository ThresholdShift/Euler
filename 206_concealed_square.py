import math

given = '1020304050607080900'
low = math.ceil(math.sqrt(int(given)))
high = math.floor(math.sqrt(1929394959697989990))

def numCheck( num ):  
    num = str(num)
    if len(num) == 19:
        for i in range(0, 19, 2):
            if num[i] != given[i]:
                return False

    return True

for i in range(low, high):
    if numCheck(i**2):
        print(i)
        break

