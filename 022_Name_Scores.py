import csv
import numpy

def Score(name, index):
    result = 0
    for i in range(len(name)):
        result = result + ord(name[i]) - 64
    return result*index

namesfile = open(r'C:\Users\jwrus_000\Google Drive\Documents\Python Scripts\Euler\022_names.txt', 'rt')
namesreader = csv.reader(namesfile, delimiter=',')
names = list(namesreader)
names = names[0] #make it a single list instead of a list containing one list of all the names
names = sorted(names) #alphabetize the names


total = 0

for j in range(len(names)):
    total = total + Score(names[j],j+1)
    

print(total)
