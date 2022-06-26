n = int(input())
s = input()
w = tuple(map(int, input().split()))
evs = []

for i in range(n):
  evs.append((w[i], int(s[i])))
evs.sort(key=lambda x:(x[0],-x[1]))
tmp = s.count('1')
ans = tmp

for i in range(n):
  if evs[i][1] == 0:
    tmp += 1
    ans = max(ans,tmp)
  else:
    tmp -= 1
print(ans)