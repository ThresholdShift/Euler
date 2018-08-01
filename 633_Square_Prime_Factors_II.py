# PE633 - Square Prime Factors II
import math

# ~~Procedure~~
# 1 - Get a list of Primes
# 2 - Square each prime.
# 3 - If the square is less than or equal to N, increment C_sum.
# 4 - If the square is less than or equal to half N, add it to a new list.
# 5 - Multiply each entry in this new list by each number in the primes list.
# 6 - Repeat from Step 3 while all entries in the new list are less than N

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



N = 10
rootN = math.floor(math.sqrt(N))

primes = list(Sieve(N))
products = primes  # Start with the products as the primes so it produces the squares of primes
newList = list((N-1,)) # Start with one entry less than N so the loop happens once
C_sum = 0

while(newList[0]<N):
    print(newList[0])
    newList = list()
    for i in primes:
        for j in products:
            prod = i*j
            if(prod<=N):
                C_sum = C_sum + 1
                if(prod<=N/2):
                    newList.append(prod)
    products.extend(newList)
    products.sort()
    

print(C_sum)



