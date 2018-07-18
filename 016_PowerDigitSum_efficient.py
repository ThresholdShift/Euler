import time
start = time.time()

x = 2**1000
total = 0

while(x>0):
    total = total + (x%10)
    x = x // 10

print(total)
print('\n',time.time()-start)
