'''Задача «Самое частое слово»
Условие
Дан текст: в первой строке задано число строк, далее идут сами строки. 
Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.'''
n = int(input())
my = {}
words = []
allwords = []
for i in range(n):
  word = input().split()
  words += word
  
for i in words:
  if i not in my:
    my[i] = 1
  else:
    my[i] += 1
    
    
maximum = max([i for i in my.values()])
minimum = min(sorted(words), key = len)

for key, val in my.items():
  #print(val, maximum, key, minimum)
  
  if val == maximum:
    allwords.append(key)
    
    
k = sorted(allwords)
print(k[0])



    
  