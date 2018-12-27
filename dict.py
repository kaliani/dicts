n = int(input())
my = {}
for i in range(n):
    user_input = input()
    key, value = user_input.split(" ")
    my[key] = value
    
print(my)