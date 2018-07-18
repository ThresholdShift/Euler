import csv

encrypted = []

with open('p059_cipher.txt') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for number in reader:
            encrypted = [encrypted, number]

encryptedNums = []

for element in encrypted[1]:
    encryptedNums.append(int(element))

xor = 0
score = []
col = 0;

for i in range(26):
    score.append([0, 0, 0])


for letter in range(97,123):
    for element in encryptedNums:
        xor = letter^element
        if (xor == ord('e') or xor == ord('t')or xor == ord('a')):
            score[letter-97][col] = score[letter-97][col]+1
        #if (xor == ord('{') or xor == ord('}')):
            #score[letter-97][col] = score[letter-97][col]-1
    
        col +=1
        if(col>2):
            col = 0
            
#for letter in range(97,123):
    #print(chr(letter), " - ", score[letter-97])


key = ['.', '.', '.']
maxval = [0, 0, 0]

for letter in range(97,123):
    for i in range(3):
        if(score[letter-97][i] > maxval[i]):
            maxval[i] = score[letter-97][i]
            key[i] = letter

message = ""
col = 0

#key = [ord('g'), ord('o'), ord('d')]
# i think the third letter is 'd'

for element in encrypted[1]:
    xor = int(element)^key[col]
    #print(element, " ^ ", key[col], " = ", xor)
    message += chr(xor)
    col += 1
    if col>2:
        col = 0


print(message)

sum = 0

for i in range(len(message)):
    sum += ord(message[i])

print(sum)
