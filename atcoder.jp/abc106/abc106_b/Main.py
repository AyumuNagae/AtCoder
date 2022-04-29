n = int(input())
ans = 0
for i in range(1, n+1, 2):
  b = 0
  for j in range(1, i+1):
    if i % j == 0: b += 1
    if b == 8: ans += 1
print(ans)