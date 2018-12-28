'''Задача «Самое частое слово»
Дан текст: в первой строке задано число строк, далее идут сами строки. 
Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.'''
n = int(input())
my_dict = {}
resultwords = []
for i in range(n):
  # Записываем все значения в словарь
  words = input().split()
  for word in words:
    if word not in my_dict:
      my_dict[word] = 1
    else:
      my_dict[word] += 1
#Находим максимальное значение повторений слова в словаре
itermax = max([i for i in my_dict.values()])
for key, val in my_dict.items():
  #Отсеиваем ключи с максимальными повторениями
  if val == itermax:
    resultwords.append(key)
#Сортируем в лексиграфическом порядке
resultwords = sorted(resultwords)
print(resultwords[0])
    
      

  