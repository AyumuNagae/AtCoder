n, a, b = map(int, input().split())
c = 0
for i in range(n+1):
  Sum = 0
  s = str(i)
  for j in s:
    Sum += int(j)
  if a<=Sum<=b:
    c += i
print(c)