from collections import OrderedDict,defaultdict

dictionary = defaultdict(int)

N = int(input())

for i in range(N):
    name,price = input().rsplit(" ",1)
    dictionary[name] += (int(price))
    
order = OrderedDict(dictionary)

for keys in order:
    print(keys,order[keys])
