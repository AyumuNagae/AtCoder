from itertools import combinations
n, p, q = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
for a, b, c, d, e in combinations(a, 5):
  if a % p * b % p * c % p * d % p * e % p == q: ans += 1
print(ans)