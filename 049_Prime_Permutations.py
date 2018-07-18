import math
import itertools
logbase = 1.005

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

def Sieve(limit):
    j = 2
    PrimeList = [True]*limit
    Primes = []

#set all of the composite number indices to False
    for i in range(2,limit):
        if PrimeList[i] == True:
            while i*j < limit:
                PrimeList[i*j] = False
                j = j+1

        j = 2
        
#create a single list containing all prime numbers under a given limit
    j = 1        
    for i in range(2, limit):
        if PrimeList[i] == True:
            Primes.append(i)
    return Primes


#function to determine if a number is prime
def PrimeCheck(num):
    degree = math.floor(math.log(num,logbase))
    PrimesList = PrimesSorted[degree]
    
    for i in range(len(PrimesList)):
        if PrimesList[i] == num:
            return True
        if PrimesList[i] > num:
            return False

    return False

#initialize prime number lists
PrimeList = Sieve(10000)
PrimesSorted = OrderedSieve(10000)


#find the low end of the 4 digit prime numbers
degree = math.floor(math.log(1000,logbase))

while len(PrimesSorted[degree]) < 1:
    degree = degree+1

LowLimit = PrimeList.index(PrimesSorted[degree][0])
results = list()

for i in range(LowLimit, len(PrimeList)):
    TempListPrimes = list()
    TempList = list(itertools.permutations(str(PrimeList[LowLimit])))
    for j in range(len(TempList)):
        if PrimeCheck(int(TempList[j])):
            TempListPrimes = TempListPrimes.append(int(TempList[j]))

    if len(TempListPrimes) >0:
        results.append(TempListPrimes)
