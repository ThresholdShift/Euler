def Sieve(limit):
    j = 2
    PrimeList = [True]*limit
    Primes = []

    for i in range(2,limit):
        if PrimeList[i] == True:
            while i*j < limit:
                PrimeList[i*j] = False
                j = j+1

        j = 2

    j = 1        
    for i in range(2, limit):
        if PrimeList[i] == True:
            Primes.append(i)

    return Primes
