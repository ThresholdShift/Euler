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
#create a single list of all the prime numbers below a certain limit
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
#begin code for Problem 27
#get a single list of primes to run through, and an ordered one for primecheck
limit = 45
Primes = Sieve(10000*limit)
PrimesSorted = OrderedSieve(10000*limit)

#make some variables to store the answers
SequenceLength = 1
a_term = 1
b_term = 1

QuadraticResult = 0

#make a for loop to cycle through different coefficients
#so a and b can be positive, negative or zero
for a_coefficient in range(-1,2):
    for b_coefficient in range(-1,2):
        for a in range(limit):
            for b in range(limit):
                for n in range(1,limit+1):
                    QuadraticResult = ((a_coefficient*Primes[a])*n)+((b_coefficient*Primes[b])*n)+n
                    print(QuadraticResult)
                    
                    if PrimeCheck(QuadraticResult) != True:
                        break #this only seems to break out of the if statement, not the for loop. starting new version with different logic
                                                                      
                    print(QuadraticResult, 'is prime')
                    if n > SequenceLength:
                        print(n, 'consecutive primes')
                        SequenceLength = n
                        a_term = a_coefficient*Primes[a]
                        b_term = b_coefficient*Primes[b]

print(a_term, 'n^2 +', b_term, 'n + n  will produce', SequenceLength, 'prime  numbers')
                        
                
                    
        
