# PE 630 - Crossed Lines
import matplotlib.pyplot as plt


#start by defining a list to find S_n
n = 100

S = [290797]
T = []

for i in range(1,2*n+1):
    S_n = S[i-1]
    S.append((S_n**2)%50515093)
    T.append((S[i]%2000)-1000)


P = []

for i in range(0, n):
    P.append((T[2*i],T[2*i+1]))



x_vals = [x[0] for x in P]
y_vals = [x[1] for x in P]


plt.plot(x_vals,y_vals,'o')
plt.show()
