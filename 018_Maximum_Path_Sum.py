import numpy

#import the csv into a numpy array
numbers = numpy.genfromtxt(r'C:\Users\jwrus_000\Google Drive\Documents\Python Scripts\Euler\018_Maximum_Path_Sum.csv', delimiter=',')

#the array will consider all blank values as NaN. So I want convert those to 0s
numbers[numpy.isnan(numbers)] = 0

col = 0
total = 0

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
    
