'''
Notes:
This is pretty much brute force. I trim it down by only looking at permutations of 1 through 9, but I think that's to be expected.
It could be sped up significantly by getting rid of all of the string manipulations and just working with integers.
'''


import itertools as it

#define a function to take a string representing a pandigital number and return
#a bool stating whether the number satisfies the Pandigital Product conditions
def PanDigital_Product(num):
    if int(num[0:2])*int(num[2:5]) == int(num[5:]) or  int(num[0:1])*int(num[1:5]) == int(num[5:]):
        return True
    else:
        return False


result = set()
PermutationsList = list(it.permutations('123456789'))
TempNum = ''


for i in range(len(PermutationsList)):
    TempNum = ''.join(PermutationsList[i])
    if PanDigital_Product(TempNum):
        result.add(int(TempNum[5:]))

print(sum(result))
