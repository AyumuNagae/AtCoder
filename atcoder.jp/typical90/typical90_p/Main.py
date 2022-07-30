n = int(input())
a, b, c = map(int,input().split())
ans = 10 ** 9
for i in range(10 ** 4):
  for j in range(10 ** 4):
    ck = n - (a * i + b * j)
    if ck % c == 0 and ck >= 0:
      ans = min(ans, i + j + ck // c)
print(ans)