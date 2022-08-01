n = int(input())
a = list(map(int, input().split()))

for i in range(n):
  a[i] -= 1

same=0; cnt=0;

for (i, j) in enumerate(a):
  if i == j:same += 1
  if i < j and a[j] == i:cnt += 1

ans = same * (same - 1) // 2 + cnt

print(ans)