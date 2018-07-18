import numpy

#import the csv into a numpy array
numbers = numpy.genfromtxt(r"C:\Users\jwrus_000\Google Drive\Documents\Python Scripts\Euler\018_Maximum_Path_Sum.csv", delimiter=",", dtype ="int")


#the array will consider all blank values as -1. So I want convert those to 0s
numbers[numpy.array(numbers)<0] = 0


col = 0
total = 0

#create another array with each number replaced with the sum of the number and every number below it
SummedNumbers = numbers.transpose().copy()
TempSum = 0

for i in range(1, len(numbers)-1):
    for j in range(len(numbers[i])):
        if numbers[i][j] > 0:
            TempSum = 0
            for k in range( len(numbers)-i):
                TempSum = TempSum + sum(numbers[i+k][j:j+k+1])

            SummedNumbers[i][j] = TempSum
            
                
for row in range(len(numbers)-1):
    total = total + numbers[row][col]
    print('+',numbers[row][col],'=',total)
    print(numbers[row+1][col],'or',numbers[row+1][col+1])
    if SummedNumbers[row+1][col] < SummedNumbers[row+1][col+1] or numbers[row+1][col] +29 < numbers[row+1][col+1]:
        col = col+1
total = total + numbers[len(numbers)-1][col]
#print(numbers[len(numbers)-1][col])



print(total)
    

