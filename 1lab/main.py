
import random

n = int(input())
m = int(input())

s = [[random.randint(1, 100) for _ in range(m)] for _ in range(n)]

print(s)
for t in s:
    print(t)

strok = [max(t) for t in s]
print(strok)

stolb = [max(s[i][j] for i in range(n)) for j in range(m)]
print(stolb)

dig = sum(s[i][i] for i in range(min(n, m)))
print(dig)

sums = [sum(t) for t in s]
r = max(sums)
k = sums.index(r)
print(k, r)