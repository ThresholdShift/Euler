import numpy
import itertools

#import the csv into a numpy array
numbers = numpy.genfromtxt(r"C:\Users\jwrus_000\Google Drive\Documents\Python Scripts\Euler\018_Maximum_Path_Sum.csv", delimiter=",", dtype ="int")


#the array will consider all blank values as -1. So I want convert those to 0s
numbers[numpy.array(numbers)<0] = 0




#determine each of the possible paths using the itertools.product() function
paths = numpy.array(list(itertools.product([0,1],repeat = 14)))

MaxSum = 0
col = 0
CurrPath = []


#using the paths array, iterate through each possible path and find the sum
for i in range(len(paths)):
    TempSum = numbers[0][0]
    col = 0
    for row in range(1,len(numbers)):
        col = col + paths[i][row-1]
        #print('row:', row,' - col:',col)
        TempSum = TempSum + numbers[row][col]

    if TempSum > MaxSum:
        MaxSum = TempSum
        CurrPath = paths[row]


i = 10

print(MaxSum)
print(CurrPath)

