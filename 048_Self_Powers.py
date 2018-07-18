#simple approach to the puzzle. I realized through the forum that I could just use a modulus to find the lowest 10 digitss

result = 0
TempNum = 0


for i in range(1,1001):
    TempNum = str(i**i)
    if len(TempNum) > 10:
        TempNum = int(TempNum[(len(TempNum)-12):])
    else:
        TempNum = int(TempNum)
    #print(i,' ---- ',result,'+',TempNum)
    result = result + TempNum

result = str(result)
print(result[len(result)-10:])
