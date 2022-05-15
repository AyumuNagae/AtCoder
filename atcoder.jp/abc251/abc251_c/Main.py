n = int(input());dic = {};

for i in range(1,n+1):
  s,p = input().split()
  p = int(p)
  if s not in dic:
    dic[s] = (-p,i)
print(min(dic.values())[1])