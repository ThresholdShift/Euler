import math
logbase = 1.005


#Generate lists of prime numbers that are indexed using a log function.
#By generating this list initially, many numbers can be checked for primality
#very quickly.
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


#A simple sieve technique to create a single long list of all prime numbers below "limit".
#This is useful for generating a list of primes to iterate through. Not as efficient for
#generating a list of primes to find a specific value in.
def Sieve(limit):
    j = 2
    PrimeList = [True]*limit
    Primes = []

    #Set all of the composite number indices to False
    for i in range(2,limit):
        if PrimeList[i] == True:
            while i*j < limit:
                PrimeList[i*j] = False
                j = j+1

        j = 2
        
    #Create a single list containing all prime numbers under a given limit
    j = 1        
    for i in range(2, limit):
        if PrimeList[i] == True:
            Primes.append(i)
    return Primes


#Function to determine if a number is prime.
#A list called PrimesSorted should be initialized using the OrderedSieve function
#before this function is used
def PrimeCheck(num):
    degree = math.floor(math.log(num,logbase))
    PrimesList = PrimesSorted[degree]
    
    for i in range(len(PrimesList)):
        if PrimesList[i] == num:
            return True
        if PrimesList[i] > num:
            return False

    return False



#Example of simple application using these tools.
num = 1000000
PrimesSorted = OrderedSieve(num+1)


if PrimeCheck(num):
    print(num, 'is prime')
else:
    print(num, 'is not prime')
