'''Задача «Самое частое слово»
Условие
Дан текст: в первой строке задано число строк, далее идут сами строки. 
Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.'''
n = int(input())
my = {}
words = []
for i in range(n):
  word = input().split()
  words += word
  
for i in words:
  if i not in my:
    my[i] = 1
  else:
    my[i] += 1
    
    
maximum = max([i for i in my.values()])


for key, val in my.items():
  if val == maximum and key == min(words, key = len):
    print(key)




    
  