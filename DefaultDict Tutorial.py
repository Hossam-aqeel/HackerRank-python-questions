from collections import defaultdict

m,n=map(int,input().split())

d=defaultdict(list)

for i in range(m):
    d['A'].append(input())
        
for i in range(n):
    d['B'].append(input())
    
    
for word in d['B']:
    indexes = [i+1 for i,x in enumerate(d['A']) if x == word]
    if indexes:
        print(*indexes)
        
    if word not in d['A']:
        print(-1)
