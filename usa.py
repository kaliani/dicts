'''Задача «Выборы в США»'''
n = int(input())
my = {}
mylist = []
for i in range(n):
  user_input = input()
  key, val = user_input.split(" ")
  if key not in my:
    my[key] = int(val)
  else:
    my[key] += int(val)
   
  
for name, val in my.items():
  mylist.append(name)
  
for i in sorted(mylist):
  print(i, my[i])