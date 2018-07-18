import csv

encrypted = []

with open('p059_cipher.txt') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for number in reader:
            encrypted = [encrypted, number]


sortedList = []
i = 0

while i<len(encrypted[1])-20:
    sortedList.append([chr(int(encrypted[1][i])), chr(int(encrypted[1][i+1])), chr(int(encrypted[1][i+2]))])
    i = i+3
    
encryptedNums = []

for element in encrypted[1]:
    encryptedNums.append(int(element))

xor = 0
score = []
alphabet = []
cnt = 1
col = 0;

for i in range(26):
    score.append([0, 0, 0])
    alphabet.append(chr(i+97))


for letter in alphabet:
    for element in encryptedNums:
        xor = int(element)^ord(letter)
        #print(cnt, " - ",chr(xor))
        cnt += 1
        if (xor == ord('e') or xor == ord('t')or xor == ord('a')):
            score[ord(letter)-97][col] = score[ord(letter)-97][col]+1

        col +=1
        if(col>2):
            col = 0
            
for letter in alphabet:
    print(letter, " - ", score[ord(letter)-97])


key = ['.', '.', '.']
maxval = [0, 0, 0]

for letter in alphabet:
    for i in range(3):
        if(score[ord(letter)-97][i] > maxval[i]):
            maxval[i] = score[ord(letter)-97][i]
            key[i] = letter

message = ""
col = 0

key = ['g', 'o', 'd']
# i think the third letter is 'd'

for element in encrypted[1]:
    xor = int(element)^ord(key[col])
    #print(element, " ^ ", key[col], " = ", xor)
    message += chr(xor)
    col += 1
    if col>2:
        col = 0


print(message)
