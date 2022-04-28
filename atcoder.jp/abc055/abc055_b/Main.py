n = int(input())
ans = 1
for i in range(n):
  ans = ans * (i+1) %1_000_000_007
print(ans)