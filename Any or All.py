t = int(input())
arr = input().split()
print(all(int(x) > 0 for x in arr) and any(x == x[::-1] for x in arr))