import math
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


num = 1000000
PrimesSorted = OrderedSieve(num+1)
PrimeList = Sieve(num)
k = 0

for i in range(33,num,2):
    test = False
    if(PrimeCheck(i) == False):
        for j in range(math.floor(math.sqrt((i-1)/2)),0, -1):
            k = i-(2*(j**2))
            if(k%1 == 0):
                if PrimeCheck(k):
                    test = True
    else:
        test = True
        
    if test == False:
        print(i)

print("done")
