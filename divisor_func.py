import math
import matplotlib.pyplot as plt

def divisorSum( num ):
    sum = 0;
    for i in range(1,math.ceil(num/2)+1):
        if(num % i == 0):
            sum += i

    return sum

x = list(range(1,10000))
y = []

for i in range(1,len(x)):
    y.append(divisorSum(x[i]))

y_norm = []

for i in range(1,len(y)):
    y_norm.append(y[i]/i)

plt.plot(y_norm)
plt.show()
