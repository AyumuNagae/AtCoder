n = int(input())
s = input()
tmp = 0
ans = 0

for i in s:
  if i == 'I': tmp += 1
  else: tmp -= 1
  ans = max(ans,tmp)
print(ans)
  