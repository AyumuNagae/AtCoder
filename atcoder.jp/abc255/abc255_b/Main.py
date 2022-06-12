n,k = map(int,input().split())
A = list(map(int,input().split()))
for i in range(k): A[i] -= 1
P = [tuple(map(int,input().split())) for _ in range(n)]
ans = 0
for x,y in P:
  t = float('inf')
  for a in A:
    p,q = P[a]
    t = min(t,(p-x)**2+(q-y)**2)
  ans = max(ans,t**0.5)
print(ans)