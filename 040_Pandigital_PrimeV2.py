import math
import numpy
import itertools
logbase = 1.005


#
#
#
#Sieve to create a list of primes that are all sorted by an index that is determined by a log and a floor function
def OrderedSieve(limit):
    j = 2
    PrimeList = [True]*limit
    PrimesSorted = []

    for i in range(1+math.floor(math.log(limit,logbase))):
        PrimesSorted.append([])
                   
    degree = 0

#set all of the composite number indices to False
    for i in range(2,limit):
        if PrimeList[i] == True:
            while i*j < limit:
                PrimeList[i*j] = False
                j = j+1

        j = 2

#create an indexed list of lists containing all prime numbers in a given range
    j = 1        
    for i in range(2, limit):
        degree = math.floor(math.log(i,logbase))
        if PrimeList[i] == True:
            PrimesSorted[degree].append(i)
    return PrimesSorted




#
#
#
#function to determine if a number is prime
def PrimeCheck(num):
    num = abs(num)
    if num == 0:
        return False

    
    degree = math.floor(math.log(num,logbase))
    PrimesList = PrimesSorted[degree]
    
    for i in range(len(PrimesList)):
        if PrimesList[i] == num:
            return True
        if PrimesList[i] > num:
            return False

    return False



'''
The number can't included digits 1 through 9 because the digits would sum to 45, making the number divisible by 3 and therefore not prime.

The same logic can be used to disregard numbers with digits 1 through 3 (sum to 6), 1 through 5 (sum to 15),
1 through 6 (sum to 21), and 1 through 8 (sum to 36). So it must be 1 through 4 (sum to 10) or 1 through 7 (sum to 28).
I'm assuming it will be 1 through 7.
'''
#
#
#
#begin code for Problem 40
#get an ordered one for primecheck
limit = 7654321
PrimesSorted = OrderedSieve(limit)

result = [] #an empty array to store all of the generated numbers that are actually prime
CurrArray = numpy.array(0) #an array that will hold each of the lists so I can use numpy functions on them


#create an array of numbers to multiply by each of the permutations to create a single 7 digit number
multiplier = numpy.array([10**6, 10**5, 10**4, 1000, 100, 10, 1])

#create a list all of the permutations of the numbers 1 through 7
NumberList = list(itertools.permutations([1,2,3,4,5,6,7]))


#create a for loop to cycle through each list, convert it into a single 7 digit number, and then check if it's prime
for i in range(len(NumberList)):
    CurrArray = numpy.array(NumberList[i]) #turn the list into a numpy array
    if PrimeCheck(numpy.sum(CurrArray * multiplier)):
        result.append(numpy.sum(CurrArray * multiplier))

print(numpy.amax(result))








