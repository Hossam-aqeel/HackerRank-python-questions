from collections import deque

n = int(input())
d = deque()

for i in range(n):
        column = input().split()
        
        match column[0]:
            case "append":
                d.append(int(column[1]))
            
            case "appendleft":
                d.appendleft(int(column[1]))
            
            case "extend":
                d.extend(column[1:])
            
            case "extendleft":
                d.extendleft(column[1:])
            
            case "remove":
                d.remove(int(column[1]))
                
            case "rotate":
                d.rotate(int(column[1]))
                
            case "pop":
                d.pop()
                
            case "popleft":
                d.popleft()
                
            case "reverse":
                d.reverse()
                
            case "clear":
                d.clear()

print (" ".join(map(str,d)))
