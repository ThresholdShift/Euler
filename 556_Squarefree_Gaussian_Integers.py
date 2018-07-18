import math
import numpy as np
logbase = 1.005
UpperLimit = 11


#----------------------------------------------------------------------------
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



PrimesList = Sieve(UpperLimit)
PrimesSorted = OrderedSieve(UpperLimit)
#---------------------------------------------------------------------------------------


#function to determine if a number is standard integer. just a shorthand to save time
def IsInt(num):
    if num%1==0:
        return True
    else:
        return False


#function to determine the gaussian quotient.
def GaussianQuotient(z1, z2):
    denom = z2[0]**2 + z2[1]**2
    print(denom)
    a3 = (z1[0]*z2[0] + z1[1]*z2[1])/denom
    b3 = (z2[0]*z1[1] - z1[0]*z2[1])/denom

    if IsInt(a3) and IsInt(b3):
        return [a3, b3]
    else:
        return 'undefined'


#function to determine if a number has a perfect square factor.
#create a list of primes, then iterate through the list and see if the squares divide evenly into the given magnitude.
def SquareFactor(num):
    i = 0
    while PrimesList[i] < num and i+1 < len(PrimesList):
        if num % (PrimesList[i]**2) ==0:
            return True
        else:
            i = i+1
    return False

result = 0


for i in range(1,int(math.ceil(math.sqrt(UpperLimit)))):
    for j in range(0,int(math.ceil(math.sqrt(UpperLimit - i**2)))):
        Square = False
        if SquareFactor((i**2) + (j**2)) and ((2*math.pi)/(np.arctan(j/i)))%1 == 0:
            j = UpperLimit - i**2 -1
            Square = True
        if Square == False:
            print(i,'+',j,'i -----',result)
            result = result + 1

    

print(result,'results')



