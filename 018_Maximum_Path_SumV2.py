import numpy

#define a function to look ahead by a given number of steps and see which path yields the higher result
#the output will be a 0 or a 1. A 0 means to turn left, and a 1 means to turn right
def LookAhead(numberarray, row, col):

    MaxSums = [0,0]
    TempMax = [0,0,0,0]
    
    for i in range(2):
        for j in range(4):
            #print(TempMax)
            #TempMax[j] = TempMax[j] + numberarray[row][col+j]
            for k in range(4-j):
                print(TempMax)
                TempMax[j] = TempMax[j] + numberarray[row+k][col+j]

        print(TempMax)
        MaxSums[i] = max(TempMax)

    
    return numpy.argmax(MaxSums)            
                      

#import the csv into a numpy array
numbers = numpy.genfromtxt(r'C:\Users\jwrus_000\Google Drive\Documents\Python Scripts\Euler\018_Maximum_Path_Sum.csv', delimiter=',')

#the array will consider all blank values as NaN. So I want convert those to 0s
numbers[numpy.isnan(numbers)] = 0

col = 0
total = 0

'''
for row in range(len(numbers)-1):
    total = total + numbers[row][col]
    #print(numbers[row][col])
    if numbers[row+1][col] < numbers[row+1][col+1]:
        col = col+1
total = total + numbers[len(numbers)-1][col]
#print(numbers[len(numbers)-1][col])

for row in range(0,15):
    print(numpy.argmax(numbers[row]))

print(total)
'''

print(LookAhead(numbers, 0,0))
