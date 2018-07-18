import math

#a function to take a string and determine if it's a palindrome
def IsPalindrome(NumString):
    if NumString[1] == 'b':
        NumString = NumString[2:] #test if it's a binary number with '0b' header, and remove it
    
    for i in range(math.ceil(len(NumString)/2)):
        if NumString[i] != NumString[len(NumString)-i-1]:
            return False

    return True


Total = 0

for i in range(11,1000000,2):
    if IsPalindrome(str(i)) and IsPalindrome(bin(i)):
        Total = Total + i


print(Total)
