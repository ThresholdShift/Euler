import matplotlib.pyplot as plt
import numpy as np

def riffle(n, k):
    if(k <= n//2):
        return 2*k - 1
    elif(k> n//2 ):
        return n-2*(n-k)
    else:
         return k





def s_n(n, k=2, limit = 61):
    k=2
    k_riffle = riffle(n,k)
    shuffles = 1
    while(k_riffle != k)&(shuffles<limit):
        k_riffle = riffle(n,k_riffle)
        shuffles = shuffles+1

    return shuffles





n = 1002


target = 60
sum_60s = 0
hits = []

for i in range(2*10**7, 4*10**7):
    if(s_n(2*i) == target):
        sum_60s = sum_60s + 2*i
        hits.append(2*i)

print(sum_60s)

plt.plot(hits,'o')
plt.show()

"""
# Create some plots to show the behavior of the s_n function
x = np.arange(4,100000,2)
y = []
for i in range(len(x)):
    y.append(s_n(x[i],2,1000))

plt.plot(x,y, 'o')
plt.show()

# CONCLUSION: The function has a lower bound of log2(n). s_n(n) >= log2(n)
#   Furthermore, when n is a power of 2, s_n(n)= log2(n)
#   This isn't a very useful lower bound.
#
#   There are likely more lower bounding functions, as the data appear to have many patterns.
"""
