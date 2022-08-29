n = int(input())
l = list(map(int, input().split()))
l.sort()
ans = 0
for i in range(n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      ans += len( {l[i], l[j], l[k]} ) == 3 and l[i] + l[j] > l[k]
print(ans)