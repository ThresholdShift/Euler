import math

#a function to take a string and determine if it's a palindrome
def IsPalindrome(NumString):
    for i in range(math.ceil(len(NumString)/2)):
        if NumString[i] != NumString[len(NumString)-i-1]:
            return False

    return True



#function to reverse a number
def ReverseNumber(num):
    num = str(num)
    return num[::-1]

def Lychrel(num):
    for j in range(50):
        num = num + int(ReverseNumber(num))
        if IsPalindrome(str(num)):
            return True

    return False

count = 0


for k in range(1,10000):
    if Lychrel(k) == False:
        count = count + 1

print(count)
