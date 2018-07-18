#Start by building a general McCarthy Function
def McCarthy(m,k,s,n):
    if n > m:
        return n - s
    else:
        return McCarthy(m,k,s,McCarthy(m,k,s,n+k))


#Define a function that produces the set of all fixed point input values for a given set of McCarthy function parameters
def FixedSetSum(m,k,s):
    results = set([0])
    for i in range(m-s, m+1):
        if McCarthy(m,k,s,i) == i:
            results.add(i)
    print(i,' - ',results)
    return sum(results)

#Define a function to calculate the result of the S function
def S(p,m):
    ResultSum = 0

    for a in range(2,p+1):
        for b in range(1,a):
            ResultSum = ResultSum + FixedSetSum(m,a,b)
    return ResultSum


print(S(10,10))
