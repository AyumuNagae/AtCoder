n,k,q = map(int, input().split())
a = list(map(int, input().split()))
l = list(map(int, input().split()))
l = list(map(lambda x: x-1, l))
for i in range(q):
  if a[l[i]] == n: continue
  if a[l[i]] == a[-1]:
    a[l[i]] += 1
    continue
  if a[l[i]]+1 != a[l[i]+1]: a[l[i]] +=1
print(*a)

  