if __name__ == '__main__':
    N = int(input())
    arr = []
    
    for i in range(N):
        column = input().split()
        
        match column[0]:
            case "append":
                arr.append(int(column[1]))
            
            case "insert":
                arr.insert(int(column[1]), int(column[2]))
            
            case "print":
                print(arr)
                
            case "remove":
                arr.remove(int(column[1]))
                
            case "sort":
                arr.sort()
                
            case "pop":
                arr.pop()
                
            case "reverse":
                arr.reverse()