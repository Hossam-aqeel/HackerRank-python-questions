from itertools import product

A = map(int, input().split())
B = map(int, input().split())
catesian_product = list(product(A, B))

for i in catesian_product:
    print(i, end=" ")
