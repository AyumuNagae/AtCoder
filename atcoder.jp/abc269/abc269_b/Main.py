s = [list(input()) for i in range(10)]
a = []
b = []
for i in range(10):
  for j in range(10):
    if s[i][j] == "#":
      a.append(i)
      b.append(j)
a = list(set(a))
b = list(set(b))
a.sort()
b.sort()
print(a[0]+1,a[-1]+1)
print(b[0]+1,b[-1]+1)