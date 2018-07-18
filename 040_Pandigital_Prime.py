import math
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




#
#
#
#begin code for Problem 40
#get an ordered one for primecheck
limit = 1000000000
PrimesSorted = OrderedSieve(limit)
