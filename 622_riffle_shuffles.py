def riffle(n, k):
    if(k <= n//2):
        return 2*k - 1
    elif(k> n//2 ):
        return n-2*(n-k)
    else:
         return k





def s_n(n, k=2):
    k=2
    k_riffle = riffle(n,k)
    shuffles = 1
    while(k_riffle != k)&(shuffles<61):
        k_riffle = riffle(n,k_riffle)
        shuffles = shuffles+1

    return shuffles




"""
n = 1002

for i in range(2,n-1):
    print(s_n(n,i))

"""
sum_60s = 0

for i in range(4, 100000):
    if(s_n(2*i) == 60):
        if(s_n(2*i,3)==60):
            sum_60s = sum_60s + 2*i
        else:
            print(2*i)

print(sum_60s)

