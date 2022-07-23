n = int(input())
s = [input() for i in range(n)]
dic = {}
for i in range(n):
  dic[s[i]] = 0

for i in range(n):
  if   dic[s[i]] == 0:print(s[i])
  else: print(s[i]+"("+str(dic[s[i]])+")")
  dic[s[i]] += 1
  