from collections import namedtuple
n = int(input())
student = namedtuple('Student', input().split())
print(f"{sum([int(student(*input().split()).MARKS) for i in range(n)])/n :.2f}")
