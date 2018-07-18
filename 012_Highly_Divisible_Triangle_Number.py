#function to find all of the integer divisors of a given number
def divisors(num):
    num = int(num)
    results = list([1,num]) #start a list with the results of the search

    if num == 0:
        return [0]
    if num < 0:
        results = [-1]
        num = num * -1

    import math
    limit = math.floor(math.sqrt(num))

    for i in range(2, limit+1):
        if num%i == 0:
            results.append(i)
            results.append(int(num/i))

    results.sort()

    return results


#function to generate triangle numbers
def triangle(num):
    return num*((1+num)/2)

#
#
#
#begin code for Problem 12 - Highly Divisible Triangular Numbers
n = 1 #n is the number of divisors, we'll give it a filler number of 1 to start with
i = 1 #i is the index. I guess I could start higher, but I figure the lower numbers won't take long to scroll through

while n < 500:
    i = i+1
    n = len(divisors(triangle(i)))

print(triangle(i))



