import inflect
import string
p = inflect.engine()
sum = 0
word = ""

for i in range(1,1001):
    word = p.number_to_words(i)
    word = word.replace(" ","")
    word = word.replace("-","")
    sum = sum + len(word)

print(sum)
