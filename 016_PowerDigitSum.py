import time
start = time.time()

x = 2**1000
x = str(x)
total = 0

for i in x:
    total = total + int(i)

print(total)
print('\n',time.time()-start)
